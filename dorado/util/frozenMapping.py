"""
@author:ihc
@file:frozenMapping.py
@description:
"""
import keyword
from collections import abc


class FrozenMapping:
    """
    convert the mapping`s key to FrozenMapping`s attribute
    :param mapping:the mapping`s key must be string
    """

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            if not key.isidentifier():
                key = 'attr_' + key
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenMapping.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj
