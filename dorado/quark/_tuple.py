"""
@project:   dorado
@author:    ihc
@description: tuple example
"""


def tupleVariability():
    t1 = (1, 2, [30, 40])
    t2 = (1, 2, [30, 40])
    print('t1 == t2 is {}.'.format(t1 == t2))
    print('t1 -1 index identifier is {}.'.format(id(t1[-1])))
    t1[-1].append(99)
    print('Now t1 is {}.'.format(t1))
    print('t1 -1 index identifier is {}.'.format(id(t1[-1])))
    print('t1 == t2 is {}.'.format(t1 == t2))


tupleVariability()
