"""
@project:   dorado
@author:    ihc
@description:
"""

from collections import deque


class _Wrapper(object):
    """
    封装缓存对象
    """

    def __init__(self, cached_object, clear_function, clear_function_args=None):
        """
        初始化_Wrapper实例
        :param cached_object:
        :param clear_function:
        :param clear_function_args:
        """
        # 被缓存的对象
        self._cached_object = cached_object
        # 对象在被取出时清理函数
        self._clear_function = clear_function
        # 清理函数参数
        self._clear_function_args = clear_function_args
        # loan_time 缓存对象被取出时将会刷新此时间
        self._loan_time = 0

        self._o_ident = id(self._cached_object)

    def ident(self):
        """
        返回被缓存对象identify
        :return:
        """
        return self._o_ident

    def cached_object(self):
        """
        获取被缓存的对象
        :return:
        """
        return self.cached_object

    def __lt__(self, other):
        return not self._loan_time > other._loadtime


class ObjectPool(object):

    def __init__(self):
        self._idle_pool = deque()
        self._base_cls = None

    def loan(self):
        """
        获取缓存对象
        :return:
        """
        if len(self._idle_pool) > 0:
            wrapper = self._idle_pool.pop()
        else:
            wrapper = self._create_wrapper_object()
        return wrapper

    def _create_wrapper_object(self):
        """
        创建缓存Wrapper对象
        :return:
        """

    def _recycle_timeout(self, timeout=10):
        """
        对于被长时间占用的对象，将在timeout过后被强制回收
        :param timeout: 超时时间(单位秒)
        :return:
        """

    def recycle(self, o):
        """
        回收对象
        :param o:
        :return:
        """

    def mem_usage(self):
        """
        获取当前缓存池内存占用(单位字节)
        :return:
        """

    def contraction(self):
        """
        收缩容量
        当缓存池中有大量空闲对象时，释放一部分对象
        :return:
        """
