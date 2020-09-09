from mks_backend.serializers.gis import GisSerializer

class GesService:

    def __init__(self):
        self.serializer = GisSerializer()

    def get_xml_for_construction_objects(self, construction_objects: list) -> str:
        return self.serializer.get_xml_for_construction_objects(construction_objects)
