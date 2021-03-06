from datetime import datetime, timedelta
from random import choice, randint, randrange
from uuid import uuid4

from sqlalchemy.exc import DBAPIError

from mks_backend.FIAS import FIASService
from mks_backend.models_meta import *
from mks_backend.session import DBSession

from .utils import (
    get_first_name,
    get_middle_name,
    get_random_address,
    get_random_date,
    get_random_email,
    get_random_phone,
    get_surname,
    try_add
)


def fill_db():
    insert_mu()
    insert_oksm()

    insert_meeting_types()
    insert_leadership_positions()
    insert_zones()
    insert_realty_types()
    insert_construction_stages()
    insert_doctypes()
    insert_critical_category()
    insert_reason_stopping()

    insert_commissions()
    insert_construction_categories_and_subcategories()
    insert_construction_companies()
    insert_construction_types()
    insert_location_types()

    insert_organizations()
    insert_class_ranks()
    insert_military_ranks()
    insert_officials()

    insert_constructions()
    insert_construction_objects()

    insert_contract_statuses()
    insert_contract_worktypes()

    insert_element_types()
    insert_measure_units()
    insert_object_categories()
    insert_progress_status()
    insert_work_types()

    insert_construction_progress()
    insert_work_lists()
    insert_object_completion()
    insert_reference_history()
    insert_construction_dynamic()
    insert_military_unit_extension()
    insert_court_decisions()
    insert_court()
    insert_participant_status()
    insert_litigation()
    insert_litigation_subject()
    insert_litigation_documents()


def insert_mu():
    def try_insert(connection, inserts):
        fails = []
        for insert in inserts:
            try:
                connection.execute(insert)
            except DBAPIError as error:
                if 'is not present' in error.orig.pgerror or 'отсутствует' in error.orig.pgerror:
                    fails.append(insert)
        if fails:
            try_insert(connection, fails)

    print('INSERT MILITARY UNITS')
    with DBSession.bind.connect() as con:
        with open('mks_backend/dumps/military_unit.sql') as text:
            try_insert(con, text.readlines())


def insert_class_ranks():
    print('INSERT CLASS RANK')
    for rank in ['Младший советник', 'Советник', 'Старший советник']:
        instatance = ClassRank(fullname=rank)
        try_add(instatance)


def insert_oksm():
    print('INSERT OKSM')
    with DBSession.bind.connect() as con:
        with open('mks_backend/dumps/oksm.sql') as text:
            try:
                con.execute(text.read())
            except DBAPIError:
                pass


def insert_meeting_types() -> None:
    print('INSERT MEETING_TYPES')
    for meeting_type in ['Совещание', 'Заседание', 'Форум', 'Съезд']:
        try_add(Meeting(fullname=meeting_type))


def insert_commissions():
    print('INSERT COMMISSIONS')
    for commission in ['НДС', 'КАСКО']:
        try_add(Commission(fullname=commission, code=commission.lower()))


def insert_construction_categories_and_subcategories():
    print('INSERT CONSTRUCTION CATEGORIES AND SUBCATEGORIES')
    for category, subcategory in [
        ('Военная категория', 'Военная подкатегория'),
        ('Строительная категория', 'Строительная подкатегория'),
        ('Гражданская категория', 'Гражданская подкатегория'),
    ]:
        subcategory = ConstructionSubcategory(fullname=subcategory)
        category = ConstructionCategory(fullname=category, subcategories=[subcategory])
        try_add(category)


def insert_construction_companies():
    print('INSERT CONSTRUCTION COMPANIES')
    for company in ['АО РТИ', 'НПК ВТиСС', 'ГВСУ № 14', 'ГВСУ по специальным объектам', 'Трест Мосэлектротягстрой ОАО']:
        try_add(ConstructionCompany(fullname=company, shortname=company.lower()))


def insert_construction_types():
    print('INSERT CONSTRUCTION TYPES')
    for construction_type in ['Военный город', 'Склад', 'Ракетная установка']:
        try_add(ConstructionType(fullname=construction_type))


def insert_organizations():
    print('INSERT ORGANIZATIONS')
    already_existed = DBSession.query(Organization).all()
    names = {organization.shortname for organization in already_existed}

    for x in range(10):
        id_ = str(uuid4())
        org_sign = choice([True, False])
        history = []

        for i in range(10):
            name = 'Организация {}.{}'.format(x, i)

            history_record = OrganizationHistory(
                shortname=name,
                fullname='OOO ' + name,
                address_legal='Юридический адрес {}.{}'.format(x, i) if org_sign else None,
                address_actual='Фактический адрес {}{}'.format(x, i),
                functions='Функции {}.{}'.format(x, i),
                inn=7731347089 if org_sign else None,
                kpp=773101001 if org_sign else None,
                ogrn=1177746126040 if org_sign else None,
                begin_date=datetime.now().date() - timedelta(days=i),
                end_date=choice([None, None, datetime.now().date() - timedelta(days=i)])
            )
            history.append(history_record)

        if history[0].shortname in names:
            continue

        organization = Organization(
            organizations_id=id_,
            par_number=choice([1, 2, 3, 4, 5]),
            org_sign=org_sign,
            history=history
        )

        sub_organization = Organization(
            organizations_id=str(uuid4()),
            parent_organizations_id=id_,
            par_number=choice([1, 2, 3, 4, 5]),
            org_sign=org_sign,
            history=[OrganizationHistory(
                shortname='Суборганизация {}'.format(x),
                fullname='Суборганизация {}'.format(x),
                address_legal='Юридический адрес {}'.format(x) if org_sign else None,
                address_actual='Фактический адрес {}'.format(x),
                functions='Функции {}'.format(x),
                inn=7731347089 if org_sign else None,
                kpp=773101001 if org_sign else None,
                ogrn=1177746126040 if org_sign else None,
                begin_date=datetime.now().date(),
            )]
        )

        try_add(organization)
        try_add(sub_organization)


def insert_military_ranks():
    print('INSERT MILITARY RANKS')
    for rank in ['Полковник', 'Генерал']:
        try_add(MilitaryRank(fullname=rank))


def insert_officials():
    print('INSERT OFFICIALS')
    military_ranks = DBSession.query(MilitaryRank).all()
    class_ranks = DBSession.query(ClassRank).all()
    organizations = DBSession.query(Organization).all()

    date_gen = get_random_date()

    for _ in range(10):
        instance = Official(
            position_name=choice(['Председатель', 'Начальник']),
            surname=get_surname(),
            firstname=get_first_name(),
            middlename=get_middle_name(),
            begin_date=next(date_gen).date(),
            end_date=choice([next(date_gen).date(), None]),
            phone=get_random_phone(),
            secure_channel='TC_P-{}'.format(randint(10, 1000)),
            email=get_random_email(),
            note=choice([None, 'Примечание']),
            organization=choice(organizations),
            military_rank=choice(military_ranks),
            class_rank=choice(class_ranks)

        )

        try_add(instance)


def insert_leadership_positions():
    print('INSERT LEADERSHIP POSITIONS')
    for position in ['Полковник', 'Генерал']:
        try_add(LeadershipPosition(fullname=position, code=position.lower()))


def insert_zones():
    print('INSERT ZONES')
    for zone in ['Равнина', 'Лесополоса', 'Тундра']:
        try_add(Zone(fullname=zone))


def insert_realty_types():
    print('INSERT REALTY TYPES')
    for realty_type in ['Большая недвижимость', 'Мелкая недвижимость']:
        try_add(RealtyType(fullname=realty_type))


def insert_construction_stages():
    print('INSERT CONSTRUCTION STAGES')
    for stage in ['Начало', 'Середина', 'Конец']:
        try_add(ConstructionStage(fullname=stage, code=stage.lower()))


def insert_doctypes():
    print('INSERT DOCTYPES')
    for doctype in ['РНС', 'ЗГЭ-ПД', 'ЗГЭ-СД', 'ЗОС', 'КС-14', 'КС-14 предварительный', 'РНВ', 'АВЭ']:
        try_add(DocType(fullname=doctype, code=doctype.lower()))


def insert_location_types():
    print('INSERT LOCATION TYPES')
    for location_type in ['Равнина', 'Лес', 'Горы', 'Тундра']:
        try_add(LocationType(fullname=location_type))


def insert_constructions():
    print('INSERT CONSTRUCTIONS')
    commissions = DBSession.query(Commission).all()
    construction_types = DBSession.query(ConstructionType).all()
    construction_companies = DBSession.query(ConstructionCompany).all()
    construction_categories = DBSession.query(ConstructionCategory).all()
    location_types = DBSession.query(LocationType).all()
    military_units = DBSession.query(MilitaryUnit).all()
    critical_categories = DBSession.query(CriticalCategory).all()
    organizations = DBSession.query(Organization).all()

    for code, name in [
        ('south_base', 'Южная база'), ('north_base', 'Северная база'),
        ('east_base', 'Восточная база'), ('west_base', 'Западная база'),
        ('secret_base', 'Секретная база'), ('experiment_base', 'Экспериментальная база')
    ]:
        category = choice(construction_categories)
        instance = Construction(
            project_code=code,
            project_name=name,
            is_critical=choice([True, False]),
            address_full=get_random_address(),
            note='Примечание к {}'.format(name),
            commission=choice(commissions),
            object_amount=randint(1, 5),
            construction_type=choice(construction_types),
            construction_company=choice(construction_companies),
            oksm_id=185,
            construction_category=category,
            military_unit=choice(military_units),
            military_district=choice(military_units),
            location_type=choice(location_types),
            critical_category=choice(critical_categories),
            organization=choice(organizations)
        )
        try_add(instance)


def insert_construction_objects():
    print('INSERT CONSTRUCTION OBJECTS')
    constructions = DBSession.query(Construction).all()

    for construction in constructions:
        for i in range(randint(1, 10)):
            instance = ConstructionObject(
                object_code='{project_code}-{code}'.format(project_code=construction.project_code, code=i),
                object_name='Наименование объекта {}'.format(i),
                construction_id=construction.construction_id,
                weight=randrange(1, 100),
                generalplan_number=str(randint(100, 100000)),
                building_volume=choice([None, randint(100, 100000)]),
                floors_amount=choice([None, randint(1, 10)]),
            )
            try_add(instance)


def create_fiases():
    print('INSERT FIASES')
    service = FIASService()
    suggests = service.get_suggests('облМосковская')[1:6]  # magic

    fiases = []
    for suggest in suggests:
        fias_address = service.expand_adress(suggest['aoid'])
        fiases.append(fias_address)


def insert_contract_statuses():
    print('INSERT CONTRACT STATUSES')
    for name in ['Исполнен', 'Расторгнут', 'Оплачен', 'Проект', 'Приостановлен', 'НаРасторжении', 'Действующий']:
        try_add(ContractStatus(fullname=name))


def insert_contract_worktypes():
    print('INSERT CONTRACT WORKTYPES')
    for name in [
        'Дата подписания итогового акта', 'Проведение обследования', 'Проведение инженерных изысканий',
        'Обмерные работы', 'Разработка проектной документации', 'Разработка рабочей документации',
        'Корректировка проектной документации', 'Корректировка рабочей документации',
        'Корректировка проектно-сметной документации', 'Строительно-монтажные работы', 'Авторский надзор',
        'Получение положительного заключения ГЭ', 'Технологическое присоединение', 'Пуско-наладочные работы',
        'Акт приемки законченного строительством объекта', 'Разработка градостроительной документации',
        'Корректировка градостроительной документации', 'Подготовительные работы', 'Благоустройство территории',
        'Работы по дооснащению объекта', 'Поставка оборудования мебели'
    ]:
        try_add(ContractWorkType(fullname=name))


def insert_element_types():
    print('INSERT ELEMENT TYPES')
    for name in ['Фундамент', 'Крыша', 'Стены', 'Подвал']:
        try_add(ElementType(fullname=name))


def insert_measure_units():
    print('INSERT MEASURE UNITS')
    for code, name in [('kg', 'килограмм'), ('t', 'тонны'), ('litres', 'Литры')]:
        try_add(MeasureUnit(unit_code=code, unit_name=name))


def insert_object_categories():
    print('INSERT OBJECT CATEGORIES')
    for name in ['Малый объект', 'Средний объект', 'Большой объект']:
        try_add(ObjectCategory(fullname=name))


def insert_progress_status():
    print('INSERT PROGRESS STATUSES')
    for name in ['Начальный статус', 'Финальный статус', 'Рабочий статус']:
        try_add(ProgressStatus(fullname=name))


def insert_work_types():
    print('INSERT WORK TYPES')
    for name in ['Закладка фундамента', 'Залитие бетона', 'Укладка асфальта']:
        try_add(WorkType(fullname=name))


def insert_construction_progress():
    print('INSERT CONSTRUCTION PROGRESS')
    objects = DBSession.query(ConstructionObject).all()
    statuses = DBSession.query(ProgressStatus).all()

    for construction_object in objects:
        for i in range(5):
            construction_progress = ConstructionProgress(
                reporting_date=(datetime.now() - timedelta(days=i)).date(),
                people_plan=randint(10, 1000),
                equipment_plan=randint(10, 1000),
                readiness=randint(1, 100),
                people=randint(10, 1000),
                equipment=randint(10, 1000),
                construction_object=construction_object,
                progress_status=choice(statuses)
            )
            try_add(construction_progress)


def insert_work_lists():
    print('INSERT WORK LISTS')
    objects = DBSession.query(ConstructionObject).all()
    work_type = DBSession.query(WorkType).all()
    element_types = DBSession.query(ElementType).all()
    measure_units = DBSession.query(MeasureUnit).all()

    for construction_object in objects:
        for i in range(4):
            work_list = WorkList(
                begin_date=(datetime.now() - timedelta(days=i)).date(),
                relevance_date=datetime.now().date(),
                element_type=choice(element_types),
                weight=randint(1, 100),
                end_date=(datetime.now() + timedelta(days=i)).date(),
                plan=randint(80, 100),
                fact=80 - randint(1, 20),
                measure_unit=choice(measure_units),
                work_type=choice(work_type),
                construction_object=construction_object,
            )
            try_add(work_list)


def insert_object_completion():
    print('INSERT OBJECT COMPLETION')
    objects = [instance.construction_objects_id for instance in DBSession.query(ConstructionObject).all()]

    for k, construction_objects_id in enumerate(objects):
        for i in range(k + 5, k * 10, k + 2):
            instance = ObjectCompletion(
                planned_date=(datetime.now() + timedelta(days=i)).date(),
                update_datetime=datetime.now() - timedelta(days=i),
                construction_objects_id=construction_objects_id
            )

            try_add(instance)


def insert_reference_history():
    print('INSERT REFERENCE HISTORY')
    objects = DBSession.query(ConstructionObject).all()

    construction_ids = {construction_object.construction_id for construction_object in objects}
    for construction_object in objects:
        available_ids = filter(lambda x: x != construction_object.construction_id, construction_ids)
        for i in available_ids:
            instance = ReferenceHistory(
                end_date=(datetime.now() - timedelta(days=i)).date(),
                construction_objects_id=construction_object.construction_objects_id,
                construction_id=i
            )
            try_add(instance)


def insert_construction_dynamic():
    print('INSERT CONSTRUCTION DYNAMIC')
    constructions = DBSession.query(Construction).all()

    for construction in constructions:
        for i in range(1, 6):
            instance = ConstructionDynamic(
                construction_id=construction.construction_id,
                reporting_date=(datetime.now() - timedelta(days=i)).date(),
                from_sakura=choice([True, False]),
                people=randint(10, 1000),
                people_plan=randint(10, 1000),
                equipment=randint(10, 1000),
                equipment_plan=randint(10, 1000),
                description='Описание хода строительсвта {}'.format(construction.project_code),
                reason='Причина {}'.format(construction.project_code),
                problems='Проблемы {}'.format(construction.project_code),
            )
            try_add(instance)


def insert_critical_category():
    print('INSERT CRITICAL CATEGORY')
    for name in ['Очень критичная', 'Не очень критичная', 'Умеренно критичная']:
        try_add(CriticalCategory(fullname=name))


def insert_reason_stopping():
    print('INSERT REASON STOPPING')
    for name in ['1ая причина', '2ая причина', '3ая причина']:
        try_add(ReasonStopping(fullname=name))


def insert_court():
    print('INSERT COURTS')
    for name in ['Верховный суд', 'Арбитражный суд', 'Конституционный суд']:
        try_add(Courts(fullname=name))


def insert_court_decisions():
    print('INSERT COURT DECISIONS')
    for name in ['Решение верховного суда', 'Решение арбитражного суда ', 'Решение конституционного суда']:
        try_add(CourtDecision(fullname=name))


def insert_military_unit_extension():
    print('INSERT MILITARY UNIT EXTENSION')
    for name in ['Добавление танка', 'Добавление БТР', 'Добавление БМП']:
        try_add(MilitaryUnitExtension(report_name=name))


def insert_participant_status():
    print('INSERT PARTICIPANT STATUS')
    for name in ['Истец (заявитель)', 'Ответчик']:
        try_add(ParticipantStatus(fullname=name))


def insert_litigation():
    print('INSERT LITIGATION')
    courts = DBSession.query(Courts).all()
    organizations = DBSession.query(Organization).all()
    participant_statuses = DBSession.query(ParticipantStatus).all()
    construction_companies = DBSession.query(ConstructionCompany).all()
    court_decisions = DBSession.query(CourtDecision).all()

    for _ in range(5):
        instance = Litigation(
            appeal_date=datetime.now().date(),
            courts_id=choice(courts).courts_id,
            organizations_id=choice(organizations).organizations_id,
            participant_statuses_id=choice(participant_statuses).participant_statuses_id,
            construction_companies_id=choice(construction_companies).construction_companies_id,
            participant_other=choice(['Участник со стороны МО', 'Участник со стороны ФНС', 'Участник со стороны МВД']),
            information='Информация',
            court_decisions_id=choice(court_decisions).court_decisions_id,
            decision_date=datetime.now().date(),
            note='Примечание'
        )
        try_add(instance)


def insert_litigation_subject():
    print('INSERT LITIGATION SUBJECT')

    litigations = DBSession.query(Litigation).all()
    constructions = DBSession.query(Construction).all()
    for construction in constructions:
        instance = LitigationSubject(
            litigation_id=choice(litigations).litigation_id,
            construction_id=construction.construction_id
        )
        try_add(instance)


def insert_litigation_documents():
    print('INSERT LITIGATION DOCUMENTS')

    litigation = DBSession.query(Litigation).all()
    doctypes = DBSession.query(DocType).all()

    for _ in range(3):
        instance = LitigationDocument(
            litigation_id=choice(litigation).litigation_id,
            doctypes_id=choice(doctypes).doctypes_id,
            doc_number=choice([1, 2, 3]),
            doc_date=datetime.now().date(),
            doc_name=choice(['Alfa', 'Beta', 'Gamma']),
            note=choice(['Документ по судебным спорам МО', 'Документ по судебным спорам ФНС',
                        'Документ по судебным спорам КС']),
            idfilestorage=None,
            upload_date=datetime.now().date()
        )
        try_add(instance)
