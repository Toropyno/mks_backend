from mks_backend.models.documents.doc_type import DocType
from mks_backend.repositories.documents.doc_type import DocTypeRepository


class DocTypeService:

    def __init__(self):
        self.repo = DocTypeRepository()

    def get_all_doc_types(self) -> list:
        return self.repo.get_all_doc_types()

    def add_doc_type(self, doc_type: DocType) -> None:
        return self.repo.add_doc_type(doc_type)

    def get_doc_type_by_id(self, id: int) -> DocType:
        return self.repo.get_doc_type_by_id(id)

    def delete_doc_type_by_id(self, id: int) -> None:
        self.repo.delete_doc_type_by_id(id)

    def update_doc_type(self, doc_type: DocType) -> None:
        self.repo.update_doc_type(doc_type)
