import os
import sys

from pyramid.paster import get_appsettings, setup_logging

from sqlalchemy import engine_from_config
from sqlalchemy.schema import CreateSchema
from sqlalchemy.engine import Engine

from mks_backend.session import Base, DBSession
from mks_backend.db_schemas import SCHEMAS

# Do not delete import models

from mks_backend.models.protocols.protocol import Protocol
from mks_backend.models.filestorage import Filestorage
from mks_backend.models.protocols.meeting import Meeting

from mks_backend.models.constructions import Commission
from mks_backend.models.constructions import Construction
from mks_backend.models.constructions import ConstructionCategory
from mks_backend.models.construction_object import ConstructionObject
from mks_backend.models.construction_stage import ConstructionStage
from mks_backend.models.constructions import ConstructionSubcategory
from mks_backend.models.military_unit.military_unit import MilitaryUnit
from mks_backend.models.object_category import ObjectCategory
from mks_backend.models.object_category_list import ObjectCategoryList
from mks_backend.models.constructions import SubcategoryList
from mks_backend.models.zone import Zone
from mks_backend.models.construction_company import ConstructionCompany
from mks_backend.models.oksm import OKSM
from mks_backend.models.constructions import ConstructionType
from mks_backend.models.realty_type import RealtyType
from mks_backend.models.work_list.work_type import WorkType
from mks_backend.models.work_list.work_list import WorkList

from mks_backend.models.military_unit.combatarm import Combatarm
from mks_backend.models.military_unit.keyword import Keyword
from mks_backend.models.military_unit.militarycity import MilitaryCity
from mks_backend.models.military_unit.namemilitaryunit import NameMilitaryUnit
from mks_backend.models.military_unit.purposemu import PurposeMU
from mks_backend.models.military_unit.sortarmedforces import SortArmedForces

from mks_backend.models.coordinate import Coordinate
from mks_backend.models.constructions import LocationType

from mks_backend.models.documents.object_document import ObjectDocument
from mks_backend.models.documents.construction_document import ConstructionDocument
from mks_backend.models.documents.doc_type import DocType

from mks_backend.models.construction_progress import ConstructionProgress
from mks_backend.models.progress_status import ProgressStatus
from mks_backend.models.work_list.measure_unit import MeasureUnit
from mks_backend.models.object_file import ObjectFile

from mks_backend.models.trips.work_trip import WorkTrip
from mks_backend.models.trips.leadership_position import LeadershipPosition
from mks_backend.models.trips.visited_object import VisitedObject

from mks_backend.models.work_list.element_type import ElementType

from mks_backend.models.inspections.inspection import Inspection
from mks_backend.models.inspections.inspection_file import InspectionFile
from mks_backend.models.inspections.inspected_object import InspectedObject

from mks_backend.models.organizations.organization import Organization
from mks_backend.models.organizations.organization_history import OrganizationHistory
from mks_backend.models.organizations.organization_document import OrganizationDocument
from mks_backend.models.organizations.official import Official
from mks_backend.models.organizations.military_rank import MilitaryRank

from mks_backend.models.state_contracts import Contract
from mks_backend.models.state_contracts import ContractStatus
from mks_backend.models.state_contracts import ContractWorkType
from mks_backend.models.state_contracts.completion_date import CompletionDate

from mks_backend.models.fias import FIAS

from mks_backend.models.miv.storage import Storage

from mks_backend._loggers import MIVLog
from mks_backend._loggers import DBError


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    create_schemas(engine)
    Base.metadata.create_all(engine)


def create_schemas(engine: Engine) -> None:
    for schema in SCHEMAS:
        if not engine.dialect.has_schema(engine, schema):
            engine.execute(CreateSchema(schema))
