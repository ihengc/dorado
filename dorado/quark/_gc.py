# coding=utf-8
"""
@project:   dorado
@author:    ihc
@description:

cPython 使用引用计数，python中使用del解除引用。当引用计数为0时，对象会被立即销毁。
注意区分变量和地址。

gc.get_count()
"""

import io
import gc
import sys
import datetime

_gc_log = []


class GcFile(io.FileIO):

    def __init__(self, name, model):
        super(GcFile, self).__init__(name, model, closefd=True)

    def write(self, p_buf):
        global _gc_log
        _gc_log.append(p_buf)
        if len(_gc_log) >= 18:
            n_buf = "[{}]INFO:{}\n".format(datetime.datetime.now(),
                                           ''.join([i.replace('\n', '') for i in _gc_log]))
            _gc_log = []
            super(GcFile, self).write(n_buf)


def gc_debug(name='gc.log'):
    file = GcFile(name, 'a')
    sys.stderr = file

    gc.set_debug(gc.DEBUG_STATS)
    for i in range(10):
        gc.collect()


gc_debug()
