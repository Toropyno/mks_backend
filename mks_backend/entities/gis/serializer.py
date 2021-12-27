from mks_backend.entities.construction_objects.construction_object import ConstructionObjectSerializer


class GisSerializer:

    def __init__(self):
        self.construction_object_serializer = ConstructionObjectSerializer()

    def get_xml_for_construction_objects(self, construction_objects: list) -> str:
        xml_for_all = ''
        xml_for_all += self.get_headers_for_xml()
        for construction_object in construction_objects:
            xml_for_all += self.get_constructions_object_info_xml(construction_object)
        xml_for_all += self.get_footers_for_xml()
        return xml_for_all

    def get_headers_for_xml(self):
        return '<?xml version="1.0" encoding="utf-8"?>' \
               '<Objects' \
               '	alias="Объекты"' \
               '	descr="Необязательное описание"' \
               '	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' \
               '	xsi:noNamespaceSchemaLocation="htsts.xsd"' \
               '	xmlns:gml="http://www.opengis.net/gml"><!-- http://debian/GML-3.1.1 -->' \
               '	<Object alias="Объект">'

    def get_footers_for_xml(self):
        return '</Objects>'

    def get_constructions_object_info_xml(self, construction_object):
        """
        надо ли нам адресная привязка по военному адресу?
        адресная привязка - может происходить по военному адресу
        раздел military
        hq - наименование штаба
        vo - наименование военного округа
        tg - наименование территориального гарнизона
        lg - наименование локального гарнизона
        vch - номер воинской части
        """

        # общая информация по объекту
        xml_for_one = '<Object alias="Объект">'
        serialized_construction_object = self.construction_object_serializer.to_json(construction_object)
        xml_for_one += '<id alias = "Идентификатор объекта в ИС">' + \
                       str(serialized_construction_object['id']) + \
                       '</id>'
        xml_for_one += '<system_id alias="Идентификатор системы">' + \
                       str('Идентификатор нашей системы - нам скажут из ГИП, когда зарегают') + \
                       '</system_id>'

        # информация по позиции объекта
        xml_for_one += '<location alias = "Привязка объекта">'

        # для location типа geometry - реальные координаты объекта
        xml_for_one += '<geometry alias = "Географическая привязка объекта">' \
                       '<geometry_epsg alias = "Код EPSG системы координат" >4326</geometry_epsg>' \
                       '<geometry_type alias = "Тип геометрии" >0</geometry_type>' \
                       '<geometry_gml></geometry_gml'

        xml_for_one += '</location>'

        # визуализация объекта - отображение значка
        xml_for_one += '<class_id alias = "Код знака">' + 'Код знака от ГИПа' + '</class_id>'
        # как пример - 00999100100401060001000000010001
        xml_for_one += '<sign_angle alias = "Угол наклона знака">0</sign_angle>',

        # базовая информация по объекту
        xml_for_one += '<name>' + '</name>'  # полное наименование
        xml_for_one += '<label>' + '</label>'  # подпись объекта
        xml_for_one += '<value>' + '</value>'  # значащая величина, характерная для объекта
        xml_for_one += '<operation>' + '</operation>'  # операция над объектом: 0 - inserted, 1 - updated, 2 - deleted)
        xml_for_one += '<link>' + '</link>'  # ссылка для запроса карточки объекта
        xml_for_one += '<lifetime>' + '</lifetime>'  # время хранения объекта в ГИП в днях

        # атрибуты объекта
        xml_for_one += '<attributes>'
        #  все необходимые атрибуты объекта/проекта
        # отдельный атрибут  '<attribute name="" alias="" type="" ></attribute>'
        xml_for_one += '</attributes>'

        xml_for_one += '</Object>'
        return xml_for_one
