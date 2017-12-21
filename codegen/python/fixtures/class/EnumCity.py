"""
Auto-generated class for EnumCity
"""
from .EnumEnumCityEnum_homeNum import EnumEnumCityEnum_homeNum
from .EnumEnumCityEnum_parks import EnumEnumCityEnum_parks
from six import string_types

from . import client_support


class EnumCity(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type enum_homeNum: EnumEnumCityEnum_homeNum
        :type enum_parks: EnumEnumCityEnum_parks
        :type name: str
        :rtype: EnumCity
        """

        return EnumCity(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'EnumCity'
        data = json or kwargs

        # set attributes
        data_types = [EnumEnumCityEnum_homeNum]
        self.enum_homeNum = client_support.set_property(
            'enum_homeNum', data, data_types, False, [], False, True, class_name)
        data_types = [EnumEnumCityEnum_parks]
        self.enum_parks = client_support.set_property(
            'enum_parks', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.name = client_support.set_property('name', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
