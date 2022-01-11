from .model import OrganizationDocument

from mks_backend.entities.BASE.serializer import BaseSerializer
from mks_backend.entities.documents.doc_type import DocTypeSerializer
from mks_backend.entities.filestorage import FileStorageSerializer

from mks_backend.utils.date_and_time import get_date_string, get_date_time_string


class OrganizationDocumentSerializer(BaseSerializer):

    def to_json(self, organization_document: OrganizationDocument) -> dict:
        return {
            'id': organization_document.organization_documents_id,
            'docType': DocTypeSerializer().to_json(organization_document.doc_type),
            'docDate': get_date_string(organization_document.doc_date),
            'docNumber': organization_document.doc_number,
            'docName': organization_document.doc_name,
            'note': organization_document.note,
            'file': FileStorageSerializer.to_json(organization_document.file_storage),
            'uploadDate': get_date_time_string(organization_document.upload_date),
            'organizationId': organization_document.organizations_id,
        }
