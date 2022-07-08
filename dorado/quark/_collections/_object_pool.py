"""
@author:Ihc
@file:_object_pool.py
@date:2022/7/7 20:32
@description:
"""
import sys
from collections import deque


class Singleton(type):

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            instance = super(Singleton, cls).__call__(*args, **kwargs)
            setattr(cls, '_instance', instance)
        return getattr(cls, '_instance')


class ObjectPool(object):
    __metaclass__ = Singleton

    def __init__(self, base_class, init_function, init_size=None, lazy_create=False, base_class_args=None,
                 init_function_args=None):

        """
        Initializes a new ObjectPool instance.
        """
        self._lazy_create = lazy_create
        if init_size is None:
            self._lazy_create = True

        if init_size <= 0:
            raise ValueError("initial_size must be greater than 0")
        else:
            if self._lazy_create:
                raise ValueError("lazy_create must be false")

        self._init_size = init_size
        self._idle_pool = deque()
        self._active_pool = deque()

        self._base_class = base_class
        self._base_class_args = base_class_args

        self._init_function = init_function
        self._init_function_args = init_function_args

        if not self._lazy_create:
            self._initialize_pool()

    def _initialize_pool(self):
        """
        initialize object pool.
        """
        for i in range(self._init_size):
            o = self._create_object()
            self._idle_pool.appendleft(o)

    def loan(self):
        """
        get object for the pool.
        """
        if len(self._idle_pool) > 0:
            o = self._idle_pool.popleft()
            self._active_pool.appendleft(o)
        else:
            o = self._create_object()
            self._active_pool.appendleft(o)
        if not self._init_function_args:
            self._init_function(o)  # assert the o is not None
        else:
            self._init_function(o, *self._init_function_args)
        return o

    def recycle(self, o):
        """
        recycle object, assert o is the base class instance.
        """
        self._idle_pool.appendleft(o)
        self._active_pool.remove(o)

    def recycle_by_base_class(self, o):
        """recycle object if o is the base class instance"""
        if isinstance(o, self._base_class):
            self._idle_pool.appendleft(o)
            self._active_pool.remove(o)

    def _create_object(self):
        """
        create object base on base_cls.
        """
        if not self._base_class_args:
            return self._base_class()
        return self._base_class(*self._base_class_args)

    def count(self):
        """
        return the numbers of objects in the pool.
        """
        return len(self._idle_pool) + len(self._active_pool)

    def mem_usage(self):
        """
        the memory size of the pool(byte),
        return tuple(idle pool memory usage, active pool usage).
        """
        return sys.getsizeof(self._idle_pool), sys.getsizeof(self._active_pool)

    def idle_count(self):
        """
        return the number of idle objects.
        """
        return len(self._idle_pool)

    def active_count(self):
        """
        return the number of active objects.
        """
        return len(self._active_pool)
