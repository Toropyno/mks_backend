import sys

from random import choice, randint, randrange
from datetime import datetime, timedelta
from typing import List
from uuid import uuid4

from faker import Faker
from sqlalchemy.exc import DBAPIError

from mks_backend.models import *
from mks_backend.services.fias import FIASService
from mks_backend.session import DBSession, bind_session, get_engine_by_uri


def fill_db(config_uri=sys.argv[-1]):
    engine = get_engine_by_uri(config_uri)
    bind_session(engine)

    insert_mu(engine)
    insert_oksm(engine)

    insert_meeting_types()
    insert_leadership_positions()
    insert_zones()
    insert_realty_types()
    insert_construction_stages()
    insert_doctypes()

    commissions = insert_commissions()
    construction_categories = insert_construction_categories_and_subcategories()
    companies = insert_construction_companies()
    construction_types = insert_construction_types()
    location_types = insert_location_types()
    # fiases = create_fiases()

    constructions = insert_constructions(
        commissions, construction_types,
        companies, construction_categories,
        location_types
    )
    construction_objects = insert_construction_objects(constructions)

    orgs = insert_organizations()
    ranks = insert_military_ranks()
    insert_officials(orgs, ranks)

    contract_statuses = insert_contract_statuses()
    contract_worktypes = insert_contract_worktypes()

    element_types = insert_element_types()
    measure_units = insert_measure_units()
    object_categories = insert_object_categories()
    progress_statuses = insert_progress_status()
    work_types = insert_work_types()

    insert_construction_progress(construction_objects, progress_statuses)
    insert_work_lists(construction_objects, work_types, element_types, measure_units)
    insert_object_completion(construction_objects)
    insert_reference_history(construction_objects)
    insert_construction_dynamic(constructions)

    DBSession.commit()


def insert_mu(engine):
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
    with engine.connect() as con:
        with open('mks_backend/dumps/military_unit.sql') as text:
            try_insert(con, text.readlines())


def insert_oksm(engine):
    print('INSERT OKSM')
    with engine.connect() as con:
        with open('mks_backend/dumps/oksm.sql') as text:
            try:
                con.execute(text.read())
            except DBAPIError:
                pass


def insert_meeting_types() -> None:
    print('INSERT MEETING_TYPES')
    for meeting_type in ['Совещание', 'Заседание', 'Форум', 'Съезд']:
        DBSession.add(Meeting(fullname=meeting_type))


def insert_commissions() -> List[Commission]:
    print('INSERT COMMISSIONS')
    commissions = []
    for commission in ['НДС', 'КАСКО']:
        instance = Commission(fullname=commission, code=commission.lower())
        commissions.append(instance)
        DBSession.add(instance)
    return commissions


def insert_construction_categories_and_subcategories():
    print('INSERT CONSTRUCTION SUBCATEGORIES')
    subcategories = []
    for subcategory in ['Военная подкатегория', 'Строительная подкатегория', 'Гражданская подкатегория']:
        instance = ConstructionSubcategory(fullname=subcategory)
        subcategories.append(instance)
        DBSession.add(instance)

    print('INSERT CONSTRUCTION SUBCATEGORIES')
    categories = []
    for category in ['Военная категория', 'Строительная категория', 'Гражданская категория']:
        instance = ConstructionCategory(fullname=category, subcategories=subcategories)
        categories.append(instance)
        DBSession.add(instance)

    return categories


def insert_construction_companies():
    print('INSERT CONSTRUCTION COMPANIES')
    companies = []
    for company in ['АО РТИ', 'НПК ВТиСС']:
        instance = ConstructionCompany(fullname=company, shortname=company.lower())
        companies.append(instance)
        DBSession.add(instance)
    return companies


def insert_construction_types():
    print('INSERT CONSTRUCTION TYPES')
    construction_types = []
    for construction_type in ['Военный город', 'Склад', 'Ракетная установка']:
        instance = ConstructionType(fullname=construction_type)
        construction_types.append(instance)
        DBSession.add(instance)

    return construction_types


def insert_organizations():
    print('INSERT ORGANIZATIONS')
    all_orghanizations = []
    for x in range(1, 11):
        id_ = str(uuid4())
        org_sign = choice([True, False])
        history = []
        for i in range(1, 6):
            history_record = OrganizationHistory(
                shortname='Организация {}.{}'.format(x, i),
                fullname='Организация {}.{}'.format(x, i),
                address_legal='Юридический адрес {}.{}'.format(x, i) if org_sign else None,
                address_actual='Фактический адрес {}{}'.format(x, i),
                functions='Функции {}.{}'.format(x, i),
                inn=get_rand_int() if org_sign else None,
                kpp=get_rand_int() if org_sign else None,
                ogrn=get_rand_int() if org_sign else None,
                begin_date=datetime.now().date() - timedelta(days=i),
                end_date=choice([None, None, datetime.now().date() - timedelta(days=i)])
            )
            history.append(history_record)

        organization = Organization(
            organizations_id=id_,
            par_number=choice([1, 2, 3, 4, 5]),
            org_sign=org_sign,
            history=history
        )

        suborganization = Organization(
            organizations_id=str(uuid4()),
            parent_organizations_id=id_,
            par_number=choice([1, 2, 3, 4, 5]),
            org_sign=org_sign,
            history=[OrganizationHistory(
                shortname='Суборгнаизация {}'.format(x),
                fullname='Суборганизация {}'.format(x),
                address_legal='Юридический адрес {}'.format(x) if org_sign else None,
                address_actual='Фактический адрес {}'.format(x),
                functions='Функции {}'.format(x),
                inn=get_rand_int() if org_sign else None,
                kpp=get_rand_int() if org_sign else None,
                ogrn=get_rand_int() if org_sign else None,
                begin_date=datetime.now().date(),
            )]
        )

        DBSession.add(organization)
        DBSession.add(suborganization)

        all_orghanizations.append(organization)
        all_orghanizations.append(suborganization)
    return all_orghanizations


def insert_military_ranks():
    print('INSERT MILITARY RANKS')
    all_ranks = []
    for rank in ['Полковник', 'Генерал']:
        rank = MilitaryRank(fullname=rank)
        DBSession.add(rank)
        all_ranks.append(rank)
    return all_ranks


def insert_officials(organizations: List[Organization], military_ranks: List[MilitaryRank]):
    print('INSERT OFFICIALS')
    DBSession.flush()
    generate_name = Faker('ru_RU')

    for organization in organizations:
        for _ in range(4):
            fake = generate_name.name().split()
            if len(fake) > 3:
                fake = fake[-3:]
            elif len(fake) < 3:
                fake = ['Иванов', 'Иванович', 'Иван']

            firstname, middlename, surname = fake

            official = Official(
                position_name=choice(['Главный', 'Заместитель', 'Стажер']),
                firstname=firstname,
                middlename=middlename,
                surname=surname,
                begin_date=datetime.now().date(),
                end_date=choice([None, datetime.now().date()]),
                phone=choice([None, '910 726 07 11']),
                secure_channel='TC_P-{}'.format(randint(10, 1000)),
                email='{}@астра.ру'.format(surname),
                note=choice([None, 'Примечание']),
                organizations_id=str(organization.organizations_id),
                military_ranks_id=choice(military_ranks).military_ranks_id
            )
            DBSession.add(official)


def insert_leadership_positions():
    print('INSERT LEADERSHIP POSITIONS')
    for position in ['Полковник', 'Генерал']:
        DBSession.add(LeadershipPosition(fullname=position, code=position.lower()))


def insert_zones():
    print('INSERT ZONES')
    for zone in ['Равнина', 'Лесополоса', 'Тундра']:
        DBSession.add(Zone(fullname=zone))


def insert_realty_types():
    print('INSERT REALTY TYPES')
    for realty_type in ['Большая недвижимость', 'Мелкая недвижимость']:
        DBSession.add(RealtyType(fullname=realty_type))


def insert_construction_stages():
    print('INSERT CONSTRUCTION STAGES')
    for stage in ['Начало', 'Середина', 'Конец']:
        DBSession.add(ConstructionStage(fullname=stage, code=stage.lower()))


def insert_doctypes():
    print('INSERT DOCTYPES')
    for doctype in ['Чертеж', 'План', 'Доклад', 'Схема']:
        DBSession.add(DocType(fullname=doctype, code=doctype.lower()))


def insert_location_types():
    print('INSERT LOCATION TYPES')
    location_types = []
    for location_type in ['Равнина', 'Лес', 'Горы', 'Тундра']:
        instance = LocationType(fullname=location_type)
        location_types.append(instance)
        DBSession.add(instance)
    return location_types


def insert_constructions(commissions: list, construction_types: list,
                         construction_companies: list, construction_categories: list,
                         location_types: list):
    print('INSERT CONSTRUCTIONS')
    constructions = []
    military_units = DBSession.query(MilitaryUnit).all()
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
            # fias=choice(fiases)
        )
        constructions.append(instance)
        DBSession.add(instance)

    return constructions


def insert_construction_objects(constructions: List[Construction]):
    print('INSERT CONSTRUCTION OBJECTS')
    construction_objects = []
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
            construction_objects.append(instance)
            construction.construction_objects.append(instance)

    return construction_objects


def create_fiases():
    print('INSERT FIASES')
    service = FIASService()
    suggests = service.get_suggests('облМосковская')[1:6]  # magic

    fiases = []
    for suggest in suggests:
        fias_address = service.expand_adress(suggest['aoid'])
        fiases.append(fias_address)

    return fiases


def insert_contract_statuses():
    print('INSERT CONTRACT STATUSES')
    contract_statuses = []
    for name in ['На рассмотрении', 'Принят', 'Отклонён']:
        instance = ContractStatus(fullname=name)
        contract_statuses.append(instance)
        DBSession.add(instance)

    return contract_statuses


def insert_contract_worktypes():
    print('INSERT CONTRACT WORKTYPES')
    contract_worktypes = []
    for name in ['Доставлено в распределительный центр', 'Утилизировано', 'На рассмотрении']:
        instance = ContractWorkType(fullname=name)
        contract_worktypes.append(instance)
        DBSession.add(instance)

    return contract_worktypes


def insert_element_types() -> List[ElementType]:
    print('INSERT ELEMENT TYPES')
    element_types = []
    for name in ['Фундамент', 'Крыша', 'Стены', 'Подвал']:
        instance = ElementType(fullname=name)
        element_types.append(instance)
        DBSession.add(instance)

    return element_types


def insert_measure_units() -> List[MeasureUnit]:
    print('INSERT MEASURE UNITS')
    measure_units = []
    for code, name in [('kg', 'килограмм'), ('t', 'тонны'), ('litres', 'Литры')]:
        instance = MeasureUnit(unit_code=code, unit_name=name)
        measure_units.append(instance)
        DBSession.add(instance)

    return measure_units


def insert_object_categories() -> List[ObjectCategory]:
    print('INSERT OBJECT CATEGORIES')
    object_categories = []
    for name in ['Малый объект', 'Средний объект', 'Большой объект']:
        instance = ObjectCategory(fullname=name)
        object_categories.append(instance)
        DBSession.add(instance)

    return object_categories


def insert_progress_status() -> List[ProgressStatus]:
    print('INSERT PROGRESS STATUSES')
    progress_statuses = []
    for name in ['Начальный статус', 'Финальный статус', 'Рабочий статус']:
        instance = ProgressStatus(fullname=name)
        progress_statuses.append(instance)
        DBSession.add(instance)

    return progress_statuses


def insert_work_types() -> List[WorkType]:
    print('INSERT WORK TYPES')
    work_types = []
    for name in ['Закладка фундамента', 'Залитие бетона', 'Укладка асфальта']:
        instance = WorkType(fullname=name)
        work_types.append(instance)
        DBSession.add(instance)

    return work_types


def insert_construction_progress(objects: List[ConstructionObject], statuses: List[ProgressStatus]):
    print('INSERT CONSTRUCTION PROGRESS')
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
            DBSession.add(construction_progress)


def insert_work_lists(objects: List[ConstructionObject], work_type: List[WorkType], element_types: List[ElementType],
                      measure_units: List[MeasureUnit]):
    print('INSERT WORK LISTS')
    for construction_object in objects:
        for i in range(4):
            work_list = WorkList(
                begin_date=(datetime.now() - timedelta(days=i)).date(),
                relevance_date=datetime.now().date(),
                element_type=element_types[i],
                weight=randint(1, 100),
                end_date=(datetime.now() + timedelta(days=i)).date(),
                plan=randint(80, 100),
                fact=80 - randint(1, 20),
                measure_unit=choice(measure_units),
                work_type=choice(work_type),
                construction_object=construction_object,
            )


def insert_object_completion(objects: List[ConstructionObject]):
    print('INSERT OBJECT COMPLETION')
    for k, construction_object in enumerate(objects):
        for i in range(k+5, k*10, k+2):
            instance = ObjectCompletion(
                planned_date=(datetime.now() + timedelta(days=i)).date(),
                update_datetime=datetime.now() - timedelta(days=i),
                construction_object=construction_object
            )

            DBSession.add(instance)


def insert_reference_history(objects: List[ConstructionObject]):
    print('INSERT REFERENCE HISTORY')
    DBSession.flush()
    construction_ids = set([construction_object.construction_id for construction_object in objects])
    for construction_object in objects:
        available_ids = filter(lambda x: x != construction_object.construction_id, construction_ids)
        for i in available_ids:
            instance = ReferenceHistory(
                end_date=(datetime.now() - timedelta(days=i)).date(),
                construction_objects_id=construction_object.construction_objects_id,
                construction_id=i
            )
            DBSession.add(instance)


def insert_construction_dynamic(constructions: List[Construction]):
    print('INSERT CONSTRUCTION DYNAMIC')
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
            DBSession.add(instance)


def get_random_address():
    fake = Faker('ru_RU')
    return fake.address()


def get_rand_int():
    return str(randint(10000000, 99999999))
