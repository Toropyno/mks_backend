from mks_backend.models.state_contracts.contract import Contract


class ContractSerializer:

    def to_json(self, contract: Contract) -> dict:
        pass

    def convert_list_to_json(self, contracts: list) -> list:
        return list(map(self.to_json, contracts))

    def to_mapped_object(self, schema: dict) -> Contract:
        pass
