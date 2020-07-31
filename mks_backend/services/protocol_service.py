from mks_backend.repositories.protocols_repository import ProtocolRepository


class ProtocolService(object):

    def __init__(self):
        self.repo = ProtocolRepository()

    def get_all_protocols(self):
        return self.repo.get_all_protocols().all()

    def get_protocol_by_id(self, id):
        return self.repo.get_protocol_by_id(id)

    def add_protocol(self, protocol):
        return self.repo.add_protocol(protocol)

    def update_protocol(self, protocol):
        return self.repo.update_protocol(protocol)

    def delete_protocol_id(self, id):
        return self.repo.delete_protocol_by_id(id)
