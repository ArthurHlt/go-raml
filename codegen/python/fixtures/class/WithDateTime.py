# DO NOT EDIT THIS FILE. This file will be overwritten when re-running go-raml.

"""
Auto-generated class for WithDateTime
"""
from datetime import datetime
from six import string_types

from . import client_support


class WithDateTime(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type birth: datetime
        :type name: string_types
        :rtype: WithDateTime
        """

        return WithDateTime(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'WithDateTime'
        data = json or kwargs

        # set attributes
        data_types = [datetime]
        self.birth = client_support.set_property('birth', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.name = client_support.set_property('name', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
