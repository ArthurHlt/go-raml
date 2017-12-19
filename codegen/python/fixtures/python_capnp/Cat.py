"""
Auto-generated class for Cat
"""
import capnp
import os
from six import string_types

from . import client_support

dir = os.path.dirname(os.path.realpath(__file__))


class Cat(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type kind: str
        :rtype: Cat
        """

        return Cat(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Cat'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.kind = client_support.set_property('kind', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

    def to_capnp(self):
        """
        Load the class in capnp schema Cat.capnp
        :rtype bytes
        """
        template = capnp.load('%s/Cat.capnp' % dir)
        return template.Cat.new_message(**self.as_dict()).to_bytes()


class CatCollection:
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def new(binary=None):
        """
        Load the binary of Cat.capnp into class Cat
        :type binary: bytes. If none creates an empty capnp object.
        rtype: Cat
        """
        template = capnp.load('%s/Cat.capnp' % dir)
        struct = template.Cat.from_bytes(binary) if bin else template.Cat.new_message()
        return Cat(**struct.to_dict(verbose=True))