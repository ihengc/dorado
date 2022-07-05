"""
@project:   dorado
@author:    ihc
@description:
"""


class Singleton(type):

    def __call__(self, *args, **kwargs):
        if not hasattr(self, '_instance'):
            instance = super(Singleton, self).__call__(*args, **kwargs)
            setattr(self, '_instance', instance)
        return getattr(self, '_instance')
