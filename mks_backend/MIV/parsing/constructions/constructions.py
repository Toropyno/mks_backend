import json
import logging
from datetime import datetime
from xml.etree import ElementTree

from mks_backend.models_meta import *
from mks_backend.session import DBSession

from ..abstract_strategy import Strategy
from ..base_repository import BaseRepository

logger = logging.getLogger(__name__)


class ConstructionsParserXML(Strategy):
    """
    Класс парсер для XML "Реестр ИСП" от АС «САКУРА»

    Используются следующие обозначения:
    Тип:
        О - обязательный элемент
        Н - необязательный элемент
    Формат:
        Т – <текст (символьная строка)>
        └── Т(n-m), где: n – минимальное количество символов, m – максимальное количество символов
        N – <число (целое или дробное)>
        └── N(m.k), где m – максимальное количество знаков в числе,
            включая целую и дробную часть числа, без учета десятичной точки и знака «-» (минус),
            k – число знаков дробной части числа
        D – <дата>, дата в формате <ГГГГ-ММ-ДД> (год-месяц-день)
        К – <код>, кодовое значение по классификатору, справочнику и т.п.
        З – <значение>, значение классификатора, справочника и т.п.
        B – <булево выражение>, логический тип «Истина/Ложь»
        Z – <целое положительное число или ноль>.

        Если значением является значение записи справочника,
        то тип значения указывается следующим образом: ЗТ, ЗN и т.д.

        S - <элемент>, составной элемент (сложный элемент логической модели, который содержит вложенные элементы);
        SA – <элемент>, составной элемент, содержащий атрибут
             (сложный элемент логической модели, который содержит вложенные элементы и атрибуты);

        TODO: первосортное дерьмо, обязательно следует декомпозировать, уменьшать кол-во запрсов к БД
    """

    def __init__(self, meta: dict, payload: ElementTree.Element, *args, **kwargs):
        self.meta = meta
        self.payload = payload

        # Версия структуры XML-документа. О/Т(2, 2)
        self.version_xsd = self.payload.find('VersionXsdSсheme').text
        # Дата формирования выгрузки. О/D
        self.upload_date = self.upload_date_parsed
        # GUID выгрузки. О/Т(36-36)
        self.upload_guid = self.payload.find('UploadGUID').text
        # Рабочий год. Этот системный параметр используется при построении отчетов и вывода сведений на карту.
        self.last_document_year = self.payload.find('ГодПоследнегоДокументаПланВвода').text

        self.construction_repo = BaseRepository(Construction)
        self.construction_stage_repo = BaseRepository(ConstructionStage)
        self.construction_object_repo = BaseRepository(ConstructionObject)
        self.realty_type_repo = BaseRepository(RealtyType)
        self.construction_dynamic_repo = BaseRepository(ConstructionDynamic)
        self.construction_documents_repo = BaseRepository(ConstructionDocument)
        self.doctypes_repo = BaseRepository(DocType)

    @property
    def upload_date_parsed(self):
        raw = self.payload.find('UploadDate').text
        return datetime.strptime(raw, '%Y-%m-%d')

    def do_algorithm(self):
        projects = self.payload.find('Projects')
        for node in projects:
            self.parse_project(node)

        DBSession.commit()

    def parse_project(self, node: ElementTree.Element):
        """
        По значению из поля <ИСП><Code> ищется запись в таблице construction (сравнение с полем project_code)
        Если запись найдена, то она изменяется, иначе добавляется новая запись
        """
        # ------- Construction  ------- #
        construction = self.construction_repo.get_or_create(
            Construction.project_code, node.find('Code').text  # О/Т(1-50)
        )
        construction.project_name = node.find('ОписаниеОбъекта').text  # О/Т(0-500)

        # ------- Commission ------- #
        commission_fullname = node.find('Комиссия').text

        commission = BaseRepository(Commission).get_by_field(
            Commission.fullname, commission_fullname  # О/ЗТ
        ).first()
        if not commission:
            commission = Commission(code='не указан', fullname=commission_fullname)
        construction.commission = commission

        # ------- Construction.object_amount ------- #
        construction.object_amount = int(node.find('КоличествоЗиС').text)  # О/Z

        # ------- ConstructionCompany ------- #
        # TODO: нет описания в XML-схеме
        construction_company_repo = BaseRepository(ConstructionCompany)
        construction_company_shortname = node.find('ИсполнительРабот').text

        construction_company = construction_company_repo\
            .get_by_field(ConstructionCompany.shortname, construction_company_shortname)\
            .first()
        if not construction_company:
            construction_company = ConstructionCompany(
                shortname=construction_company_shortname, fullname=construction_company_shortname
            )
            construction_company_repo.add_to_session(construction_company)

        construction.construction_company = construction_company

        # ------- FIAS ------- #
        # TODO: FIAS
        fias_address = node.find('Местоположение')

        address_full = fias_address.find('ФактическоеМестоположение')  # Н/Т(0-200)
        construction.address_full = address_full.text if address_full else None

        # ------- Organization ------- #
        # TODO: У модели Organization нет поля fullname, оно есть только у реквизитов, поэтому это супер неэффективно
        organization_fullname = node.find('РУЗКС').text  # О/ЗТ
        organizations = BaseRepository(Organization).get_all()
        try:
            organization = next(org for org in organizations if org.fullname == organization_fullname)
        except StopIteration:
            raise ValueError('Такой организации не существует в реестре РУЗКС')
        else:
            construction.organization = organization

        construction.department = node.find('УправлениеФКП').text  # О/ЗТ
        construction.officer = node.find('ОтветственныйФКП').text  # О/ЗТ

        # ------- MilitaryDistrict ------- #
        # TODO: непонятно как искать, предварительный вариант
        military_district = fias_address.find('ВоенныйОкруг').text  # О/ЗТ
        mu_name = BaseRepository(NameMilitaryUnit).get_by_field(NameMilitaryUnit.snamemu, military_district).first()
        military_district = BaseRepository(MilitaryUnit).get_by_field(MilitaryUnit.idNameMU, mu_name.idnamemu).first()
        construction.military_district = military_district

        # ------- TechnicalSpec ------- #
        tz = node.find('НаличиеТЗ').find('ДатаУтвТЗ')  # О/D
        construction.technical_spec = bool(tz is not None and tz.text)

        # ------- PriceCalc ------- #
        tz = node.find('НаличиеРНЦ').find('ДатаСогласованияСПодрядчиком')
        construction.price_calc = bool(tz is not None and tz.text)  # О/D

        # ------- DeletionMark ------- #
        construction.deletion_mark = node.find('DeletionMark').text == 'true'  # О/B

        for construction_stage in node.find('СоставОбъекта').find('СтруктураЭтапов'):
            self.parse_construction_stage(stage=construction_stage, construction=construction)

        self.parse_construction_dynamic(construction, node)
        self.parse_construction_documents(construction, node)

    def parse_construction_stage(self, stage: ElementTree.Element, construction: Construction):
        """
        Объект строительства (здание и сооружение) определяется по значению элемента <Код> из ветки
        <СоставОбъекта><СтруктураЭтапов><Этапы><ЗданияСооружения><ЗданиеСооружение>,
        оно уникально и соответствует значению поля «Код объекта» из таблицы construction_objects

        Поиск в таблице construction_objects осуществляется только по коду объекта (без учета принадлежности к ИСП).
        Если запись найдена, то она изменяется, иначе добавляется новая запись
        Одновременно с объектами строительства наполняется словарь «Этапы строительства»
        """
        code = stage.find('Код').text

        construction_objects = stage.find('ЗданияСооружения')
        if not construction_objects:
            logger.error(
                'Некорректная запись в XML для <ЗданияСооружения> Код этапа {} выгрузка {}'
                .format(code, self.upload_guid)
            )
            return

        construction_stage = self.construction_stage_repo.get_by_field(ConstructionStage.code, code).first()
        if not construction_stage:
            parent_fullname = stage.find('ЭтапРодитель').text
            if parent_fullname:
                parent_stage = self.construction_stage_repo.get_or_create(ConstructionStage.fullname, parent_fullname)
            else:
                parent_stage = None

            construction_stage = self.construction_stage_repo.create_instance(ConstructionStage.code, code)
            construction_stage.fullname = stage.find('Этап').text
            construction_stage.hierarchy_level = stage.find('Уровень').text
            construction_stage.parent = parent_stage

        for construction_object in construction_objects:
            self.parse_construction_object(
                construction_object_raw=construction_object,
                construction=construction,
                construction_stage=construction_stage
            )
            DBSession.commit()

    def parse_construction_object(
            self,
            construction_object_raw: ElementTree.Element,
            construction: Construction,
            construction_stage: ConstructionStage
    ):
        construction_object = self.construction_object_repo.get_by_field(
            ConstructionObject.object_code, construction_object_raw.find('Код').text
        ).first()

        if not construction_object:
            # Добавление новой записи
            construction_object = self.construction_object_repo.create_instance(
                ConstructionObject.object_code, construction_object_raw.find('Код').text
            )
        else:
            # Редактирование существующей записи
            if construction_object.construction.project_code != construction.project_code:
                # Если ИСП из xml не совпадает с тем, что сохранен в базе, значит,
                # здание/сооружение переместили в другой ИСП.
                reference_history_record = ReferenceHistory(
                    construction=construction_object.construction, construction_object=construction_object
                )
                DBSession.add(reference_history_record)

        construction_object.object_name = construction_object_raw.find('Наименование').text
        construction_object.weight = construction_object_raw.find('Вес').text
        construction_object.generalplan_number = construction_object_raw.find('НомерНаГП').text

        construction_object.construction = construction
        construction_object.construction_stage = construction_stage
        construction_object.realty_type = self.realty_type_repo.get_or_create(
            RealtyType.fullname, construction_object_raw.find('ТипЗданияСооружения').text
        )

    def parse_construction_dynamic(self, construction: Construction, node: ElementTree.Element):
        construction_dynamic_raw = node.find('ХодВыполненияСМР')

        construction_dynamic = self.construction_dynamic_repo.get_by_fields(
            reporting_date=self.upload_date, from_sakura=True, construction_id=construction.construction_id
        ).first()

        if not construction_dynamic:
            construction_dynamic = self.construction_dynamic_repo.create_instance(
                ConstructionDynamic.reporting_date, self.upload_date
            )
            construction_dynamic.from_sakura = True
            construction_dynamic.construction_id = construction.construction_id

        construction_dynamic.people_plan = construction_dynamic_raw.find('КоличествоЛюдейПлан').text
        construction_dynamic.people = construction_dynamic_raw.find('КоличествоЛюдей').text
        construction_dynamic.equipment_plan = construction_dynamic_raw.find('КоличествоТехникиПлан').text
        construction_dynamic.equipment = construction_dynamic_raw.find('КоличествоТехники').text
        construction_dynamic.description = construction_dynamic_raw.find('ОписаниеХодаСМР').text
        construction_dynamic.problems = node.find('ПроблемныеВопросы').text
        construction_dynamic.update_datetime = datetime.now()

        reasons = json.loads(construction_dynamic_raw.find('ПричиныОстановкиСМР').text)
        reasons = {reason['worksStoppageReason'] for reason in reasons if reason['worksStoppageReason']}
        construction_dynamic.reason = ';'.join(reasons)

    def parse_construction_documents(self, construction: Construction, node: ElementTree.Element):
        rns_document_type = self.doctypes_repo.get_by_field(DocType.fullname, 'РНС').first()
        zge_document_type_pd = self.doctypes_repo.get_by_field(DocType.fullname, 'ЗГЭ-ПД').first()
        zge_document_type_sd = self.doctypes_repo.get_by_field(DocType.fullname, 'ЗГЭ-СД').first()
        zos_document_type = self.doctypes_repo.get_by_field(DocType.fullname, 'ЗОС').first()

        for rns_document_raw in node.find('РазрешенияНаСтроительство'):
            rns_document = self.construction_documents_repo.get_by_fields(
                construction_id=construction.construction_id,
                doctypes_id=rns_document_type.doctypes_id,
                doc_number=rns_document_raw.find('Номер').text,
                doc_date=datetime.strptime(rns_document_raw.find('Дата').text, '%Y-%m-%d')
            ).first()
            if not rns_document:
                rns_document = ConstructionDocument(
                    construction_id=construction.construction_id,
                    doctypes_id=rns_document_type.doctypes_id,
                    doc_number=rns_document_raw.find('Номер').text,
                    doc_date=datetime.strptime(rns_document_raw.find('Дата').text, '%Y-%m-%d'),
                    valid_until=datetime.strptime(rns_document_raw.find('СрокДействия').text, '%Y-%m-%d')
                )
                self.construction_documents_repo.add_to_session(rns_document)

        for zge_document_raw in node.find('ЗаключенияГосударственнойЭкспертизы'):
            if zge_document_raw.find('ТипЗаключения').text == 'ПД':
                zge_document_type = zge_document_type_pd
            else:
                zge_document_type = zge_document_type_sd

            zge_document = self.construction_documents_repo.get_by_fields(
                construction_id=construction.construction_id,
                doctypes_id=zge_document_type.doctypes_id,
                doc_number=zge_document_raw.find('Номер').text,
                doc_date=datetime.strptime(zge_document_raw.find('Дата').text, '%Y-%m-%d')
            ).first()
            if not zge_document:
                zge_document = ConstructionDocument(
                    construction_id=construction.construction_id,
                    doctypes_id=zge_document_type.doctypes_id,
                    doc_number=zge_document_raw.find('Номер').text,
                    doc_date=datetime.strptime(zge_document_raw.find('Дата').text, '%Y-%m-%d'),
                )
                self.construction_documents_repo.add_to_session(zge_document)

        for zos_document_raw in node.find('ЗОС'):
            zos_document = self.construction_documents_repo.get_by_fields(
                construction_id=construction.construction_id,
                doctypes_id=zos_document_type.doctypes_id,
                doc_number=zos_document_raw.find('Номер').text,
                doc_date=datetime.strptime(zos_document_raw.find('Дата').text, '%Y-%m-%d')
            ).first()
            if not zos_document:
                zos_document = ConstructionDocument(
                    construction_id=construction.construction_id,
                    doctypes_id=zos_document_type.doctypes_id,
                    doc_number=zos_document_raw.find('Номер').text,
                    doc_date=datetime.strptime(zos_document_raw.find('Дата').text, '%Y-%m-%d'),
                )
                self.construction_documents_repo.add_to_session(zos_document)


def main():
    with open('/home/atimchenko/PycharmProjects/mks_backend/mks_backend/MIV/parsing/constructions/sakura_isp.xml', 'r') \
            as f:
        raw_xml = f.read()

    root = ElementTree.fromstring(raw_xml)

    ConstructionsParserXML(dict(), root).do_algorithm()
