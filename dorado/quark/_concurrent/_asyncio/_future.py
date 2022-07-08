"""
@project:   dorado
@author:    ihc
@description:
"""

_PENDING = 'PENDING'  # 表示当前任务还在执行中，还为拿到结果
_CANCELLED = 'CANCELLED'  # 表示当前任务可以被取消
_FINISHED = 'FINISHED'  # 任务执行完成

# _Future的实例的数量是与需要执行的任务数量保持一致的。
# 也就是说会频发的创建_Future实例
# 任务在执行中可能会抛出异常，若任务因异常终止，我们需要从_Future中获取异常

"""
Future接口与功能

1.设置任务执行结果
2.获取任务执行的结果

3.设置任务执行的异常信息
4.获取任务执行的异常信息

5.设置任务执行完后需要执行的回调函数
6.移除任务执行完后需要执行的回调函数

7.获取任务当前执行的状态
7.1状态的定义：执行中,执行完成

8.取消任务的执行
8.1任务在何时可以被取消(任务执行到哪些阶段是不可以被取消的)
任务在执行中才可以被取消，否则不能被取消
9.任务是否已经执行完成

"""


class _Future:
    _state = _PENDING  # 任务状态
    _loop = None  # 事件循环
    _result = None  # 任务结果

    def __init__(self, loop=None):
        """

        :param loop:表示事件循环
        """
        if loop is None:
            # 获取事件循环
            pass
        self._callbacks = []  # 任务在执行完后，执行的回调函数

    def get_loop(self):
        return self._loop

    def set_result(self, result):
        self._result = result

    def get_result(self):
        return self._result
