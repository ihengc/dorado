"""
@project:   dorado
@author:    ihc
@description:
"""

from dorado.common.singleton import Singleton


class LoadedCache(metaclass=Singleton):
    """
    the class must be singleton
    """

    def __init__(self):
        self._size = 0
        self._loadedCache = set()

    def remove(self, uid):
        self._loadedCache.remove(uid)
        self._size -= 1

    def add(self, uid):
        self._loadedCache.add(uid)
        self._size += 1

    def size(self):
        return self._size

    def exists(self, uid):
        return uid in self._loadedCache

    def clear(self):
        self._loadedCache = set()
