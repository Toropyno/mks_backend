from mks_backend.models.geoobject.geo_style import GeoStyle


class GeoStyleSerialaizer:

    @classmethod
    def convert_object_to_json(cls, style: GeoStyle) -> dict:
        return {
            'id': style.geo_style_id,
            'classId': style.class_id,
            'libraryId': style.library_id,
            'classifId': style.classif_id
        }

