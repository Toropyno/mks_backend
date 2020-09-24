# from mks_backend.errors.db_basic_error import db_error_handler
# from mks_backend.models.doc_type import DocType
# from mks_backend.repositories import DBSession
#
#
# class DocTypeRepository:
#
#     def get_all_doc_types(self) -> list:
#         return DBSession.query(DocType).order_by(DocType.contract_date).all()
#
#     def get_doc_type_by_id(self, id: int) -> DocType:
#         return DBSession.query(DocType).get(id)
#
#     @db_error_handler
#     def add_doc_type(self, doc_type: DocType) -> None:
#         DBSession.add(doc_type)
#         DBSession.commit()
#
#     @db_error_handler
#     def update_doc_type(self, doc_type: DocType) -> None:
#         DBSession.query(DocType).filter_by(doc_type_id=doc_type.doc_type_id).update(
#             {
#                 'project_code': doc_type.project_code,
#                 'project_name': doc_type.project_name,
#                 'doc_type_categories_id': doc_type.doc_type_categories_id,
#             }
#         )
#         DBSession.commit()
#
#     def delete_doc_type(self, id: int) -> None:
#         doc_type = self.get_doc_type_by_id(id)
#         DBSession.delete(doc_type)
#         DBSession.commit()
