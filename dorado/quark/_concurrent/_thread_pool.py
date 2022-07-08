"""
@project:   dorado
@author:    ihc
@description:
"""
import threading


class _thread_pool(object):

    def __init__(self, max_workers=None):
        self._max_workers = max_workers
        self._work_queue = []
