"""
@project:   dorado
@author:    ihc
@description:
"""
import weakref


def weak_ref():
    set1 = {0, 1}
    s = weakref.ref(set1)
    print(s)
    print(s() is None)
    set1 = {2, 3, 4}
    print(s() is None)


weak_ref()