"""
@project:   dorado
@author:    ihc
@description:
"""


def objectIdentifier():
    m1 = dict()
    m2 = dict()
    print('object identifier m1:{} m2:{}'.format(id(m1), id(m2)))


objectIdentifier()
