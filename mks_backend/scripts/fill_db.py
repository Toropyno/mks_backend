import sys

from random import choice, randint
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

    orgs = insert_organizations()
    ranks = insert_military_ranks()
    insert_officials(orgs, ranks)

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

    with engine.connect() as con:
        with open('mks_backend/dumps/military_unit.sql') as text:
            try_insert(con, text.readlines())


def insert_oksm(engine):
    with engine.connect() as con:
        with open('mks_backend/dumps/oksm.sql') as text:
            try:
                con.execute(text.read())
            except DBAPIError:
                pass


def insert_meeting_types():
    for meeting_type in ['Совещание', 'Заседание', 'Форум', 'Съезд']:
        DBSession.add(Meeting(fullname=meeting_type))


def insert_commissions():
    commissions = []
    for commission in ['НДС', 'КАСКО']:
        instance = Commission(fullname=commission, code=commission.lower())
        commissions.append(instance)
        DBSession.add(instance)
    return commissions


def insert_construction_categories_and_subcategories():
    subcategories = []
    for subcategory in ['Военная подкатегория', 'Строительная подкатегория', 'Гражданская подкатегория']:
        instance = ConstructionSubcategory(fullname=subcategory)
        subcategories.append(instance)
        DBSession.add(instance)

    categories = []
    for category in ['Военная категория', 'Строительная категория', 'Гражданская категория']:
        instance = ConstructionCategory(fullname=category, subcategories=subcategories)
        categories.append(instance)
        DBSession.add(instance)

    return categories


def insert_construction_companies():
    companies = []
    for company in ['АО РТИ', 'НПК ВТиСС']:
        instance = ConstructionCompany(fullname=company, shortname=company.lower())
        companies.append(instance)
        DBSession.add(instance)
    return companies


def insert_construction_types():
    construction_types = []
    for construction_type in ['Военный город', 'Склад', 'Ракетная установка']:
        instance = ConstructionType(fullname=construction_type)
        construction_types.append(instance)
        DBSession.add(instance)

    return construction_types


def insert_organizations():
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
    all_ranks = []
    for rank in ['Полковник', 'Генерал']:
        rank = MilitaryRank(fullname=rank)
        DBSession.add(rank)
        all_ranks.append(rank)
    return all_ranks


def insert_officials(organizations: List[Organization], military_ranks: List[MilitaryRank]):
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
    for position in ['Полковник', 'Генерал']:
        DBSession.add(LeadershipPosition(fullname=position, code=position.lower()))


def insert_zones():
    for zone in ['Равнина', 'Лесополоса', 'Тундра']:
        DBSession.add(Zone(fullname=zone))


def insert_realty_types():
    for realty_type in ['Большая недвижимость', 'Мелкая недвижимость']:
        DBSession.add(RealtyType(fullname=realty_type))


def insert_construction_stages():
    for stage in ['Начало', 'Середина', 'Конец']:
        DBSession.add(ConstructionStage(fullname=stage, code=stage.lower()))


def insert_doctypes():
    for doctype in ['Чертеж', 'План', 'Доклад', 'Схема']:
        DBSession.add(DocType(fullname=doctype, code=doctype.lower()))


def insert_location_types():
    location_types = []
    for location_type in ['Равнина', 'Лес', 'Горы', 'Тундра']:
        instance = LocationType(fullname=location_type)
        location_types.append(instance)
        DBSession.add(instance)
    return location_types


def insert_constructions(commissions: list, construction_types: list,
                         construction_companies: list, construction_categories: list,
                         location_types: list):
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
            contract_date=datetime.now().date() - timedelta(days=randint(10, 100)),
            is_critical=choice([True, False]),
            planned_date=datetime.now().date(),
            address_full=get_random_address(),
            note='Примечание к {}'.format(name),
            commission=choice(commissions),
            object_amount=randint(1, 5),
            construction_type=choice(construction_types),
            construction_company=choice(construction_companies),
            oksm_id=185,
            construction_category=category,
            military_unit=choice(military_units),
            location_type=choice(location_types),
            # fias=choice(fiases)
        )
        constructions.append(instance)
        DBSession.add(instance)

    return constructions


def create_fiases():
    service = FIASService()
    suggests = service.get_suggests('облМосковская')[1:6]  # magic

    fiases = []
    for suggest in suggests:
        fias_address = service.expand_adress(suggest['aoid'])
        fiases.append(fias_address)

    return fiases


def get_random_address():
    fake = Faker('ru_RU')
    return fake.address()


def get_rand_int():
    return str(randint(10000000, 99999999))
