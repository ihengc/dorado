# coding=utf-8
"""
@project:   dorado
@author:    ihc
@description:
"""
import sys
from collections import deque

import gevent


class Singleton(type):

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            instance = super(Singleton, cls).__call__(*args, **kwargs)
            setattr(cls, '_instance', instance)
        return getattr(cls, '_instance')


class _Wrapper(object):

    def __init__(self, cached_object, clear_function, clear_function_args=None):
        """
        初始化_Wrapper实例
        :param cached_object: 被缓存的对象
        :param clear_function: 缓存对象清理方法
        :param clear_function_args: 清理方法参数
        """
        self._cached_object = cached_object
        self._clear_function = clear_function
        self._clear_function_args = clear_function_args

        self._g_ident = None
        self._o_ident = id(self._cached_object)

    def cached_object_ident(self):
        """
        返回缓存对象的对象标识
        :return:
        """
        return self._o_ident

    def greenlet_ident(self):
        """
        返回获取协程的唯一标识
        :return:
        """
        return self._g_ident

    def initial(self):
        """
        获取当前协程唯一标识，清理被缓存对象
        :return:
        """
        self._set_g_ident()
        self._clear()

    def cached_object(self):
        """
        获取被缓存的对象
        :return:
        """
        return self._cached_object

    def _set_g_ident(self):
        """
        获取当前协程唯一标识
        :return:
        """
        greenlet = gevent.getcurrent()
        self._g_ident = greenlet.minimal_ident

    def _clear(self):
        """
        清理被缓存对象
        :return:
        """
        if self._clear_function_args:
            self._clear_function(self._cached_object, *self._clear_function_args)
        else:
            self._clear_function(self._cached_object)

    def __str__(self):
        return '<{}({},{})>'.format(_Wrapper.__name__, self._o_ident, self._g_ident)

    def __repr__(self):
        return '<{}({},{})>'.format(_Wrapper.__name__, self._o_ident, self._g_ident)


class CoroutineObjectPool(object):
    __metaclass__ = Singleton

    def __init__(self, initial_capacity=None, lazy_create=False):
        """
        初始化CoroutineObjectPool实例
        :param initial_capacity: 对象池初始化对象个数
        :param lazy_create: 当lazy_create为true时，不会事先创建缓存对象，在获取对象时创建
            base_class是需要缓存的类型,根据base_class生成缓存对象。base_class_args为base_class
        生成实例时需要传递的初始化参数,base_class_args为元祖。
            clear_function函数用于将缓存对象属性值重置。该函数的第一个参数为缓存对象。后面参数放在
        clear_function_args中，其为元祖。
        """
        self._pool = deque()
        self._used_o_ident_set = set()
        self._used_g_ident_map = {}
        self._used_o_g_ident_map = {}

        self._lazy_create = lazy_create
        if initial_capacity is None:
            self._lazy_create = True
        else:
            if initial_capacity < 0:
                raise ValueError('initial_capacity must be greater than 0')
            else:
                if self._lazy_create is True:
                    raise ValueError('lazy_create must be false')

        self._initial_capacity = initial_capacity
        self._base_class = None
        self._clear_function = None
        self._base_class_args = None
        self._clear_function_args = None

    def _initial_pool(self):
        """
        根据初始化所给的initial_capacity创建缓存实例
        :return:
        """
        for i in range(self._initial_capacity):
            _wrapper = self._create_wrapper()
            self._pool.append(_wrapper)

    def _create_wrapper(self):
        """
        创建_Wrapper实例
        :return:
        """
        if self._base_class_args:
            cached_object = self._base_class(*self._base_class_args)
        else:
            cached_object = self._base_class()
        return _Wrapper(cached_object, self._clear_function, self._clear_function_args)

    def init_pool_from_class(self, base_class, clear_function):
        """
        初始化对象池,默认base_class创建实例时不需要额外的参数，重置缓存对象时不需要额外的参数。
        :param base_class: 使用base_class创建缓存实例
        :param clear_function:  使用clear_function将缓存对象重置
        :return:
        """
        if not base_class:
            raise ValueError('base_class must not be None')

        if not clear_function:
            raise ValueError('clear_function must not be None')

        self._base_class = base_class
        self._clear_function = clear_function

        if self._lazy_create is False:
            self._initial_pool()

    def init_pool_from_class_args(self, base_class, base_class_args, clear_function, clear_function_args):
        """
        初始化对象池
        :param base_class:
        :param base_class_args:
        :param clear_function:
        :param clear_function_args:
        :return:
        """
        if not base_class:
            raise ValueError('base_class must not be None')

        if not base_class_args:
            raise ValueError('base_class_args must not be None')

        if not clear_function:
            raise ValueError('clear_function must not be None')

        if not clear_function_args:
            raise ValueError('clear_function_args must not be None')

        self._base_class = base_class
        self._base_class_args = base_class_args

        self._clear_function = clear_function
        self._clear_function_args = clear_function_args

        if self._lazy_create is False:
            self._initial_pool()

    def loan(self):
        """
        从池中获取缓存对象
        :return:
        """
        if len(self._pool) > 0:
            _wrapper = self._pool.pop()
        else:
            _wrapper = self._create_wrapper()

        _wrapper.initial()

        self._used_g_ident_map[_wrapper.greenlet_ident()] = _wrapper
        self._used_o_g_ident_map[_wrapper.cached_object_ident()] = _wrapper.greenlet_ident()
        self._used_o_ident_set.add(_wrapper.cached_object_ident())

        return _wrapper.cached_object()

    def recycle(self, cached_object):
        """
        回收缓存对象，当可以获取到被缓存的对象时，使用此方法
        :param cached_object:
        :return: 回收成功返回True;否则返回False
        """
        # 回收对象必须是base_class的实例
        if isinstance(cached_object, self._base_class):
            # 回收对象必须在被使用中
            ident = id(cached_object)
            if ident in self._used_o_ident_set:
                self._pool.append(cached_object)

                self._used_o_ident_set.remove(ident)

                greenlet = gevent.getcurrent()
                self._used_g_ident_map.pop(greenlet.minimal_ident)
                self._used_o_g_ident_map.pop(ident)
                return True
        return False

    def recycleByCoroutineIdent(self):
        """
        当无法获取到被取出的对象时，使用此方法。
        断言对象在协程中被取出。
        :return:
        """
        greenlet = gevent.getcurrent()
        # 检查当前协程是否在对象池中拿走缓存对象
        _wrapper = self._used_g_ident_map.get(greenlet.minimal_ident)
        if _wrapper:
            # 确定缓存对象被拿走
            self._pool.append(_wrapper)
            self._used_o_ident_set.remove(_wrapper.cached_object_ident())
            self._used_o_g_ident_map.pop(_wrapper.cached_object_ident())
            self._used_g_ident_map.pop(greenlet.minimal_ident)
            return True
        return False

    def idle_count(self):
        """
        返回当前对象池中的对象个数
        :return:
        """
        return len(self._pool)

    def count(self):
        """
        返回当对象全部未使用时，被缓存对象的个数
        :return:
        """
        return len(self._pool) + len(self._used_o_ident_set)

    def mem_usage(self):
        """
        返回当前对象池所占内存大小(单位字节)
        :return:
        """
        return sys.getsizeof(self._pool) + sys.getsizeof(self)

    def approximate_mem_usage(self):
        """
        当全部缓存对象被归还时，对象池所占内存大小(单位字节)
        :return:
        """
        return (float(sys.getsizeof(self._pool)) / len(self._pool)) * (
                len(self._pool) + len(self._used_o_ident_set)) + sys.getsizeof(self)

    def __call__(self, *args, **kwargs):
        """
        直接调用loan方法，方便兼容
        :param args:
        :param kwargs:
        :return:
        """
        return self.loan()


"""
from com.metek.card.game.proto.xx_pb2 import SCMsgPush


def _SCMsgPush_clear_function(cached_object):
    cached_object.Clear()


def _initialize_SCMsgPush_pool():
    scmsgpush_pool = CoroutineObjectPool(initial_capacity=100)
    scmsgpush_pool.init_pool_from_class(base_class=SCMsgPush, clear_function=_SCMsgPush_clear_function)
    return scmsgpush_pool

pushresp = _initialize_SCMsgPush_pool

"""

if __name__ == '__main__':
    class BaseClass(object):
        pass


    def baseClassClear(cached_object):
        pass


    pool = CoroutineObjectPool(initial_capacity=10)
    pool.init_pool_from_class(base_class=BaseClass, clear_function=baseClassClear)
    assert pool.count() == 10
    gevent.spawn(pool.loan)
    gevent.sleep(0.1)
    assert pool.idle_count() == 9
    gevent.spawn(pool)
    gevent.sleep(0.1)
    assert pool.idle_count() == 8
