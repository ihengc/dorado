"""
@project:   dorado
@author:    ihc
@description: how to copy python object
"""
import copy

"""
1) shallow copy
    1) 
2) deep copy
"""


def shallowCopy():
    list1 = [3, [55, 44], (7, 8, 9, [1, 2, 3])]  # [value, reference, reference]
    list2 = list(list1)  # shallow copy only copy the object reference

    print('List1 == List2 is {}.'.format(list1 == list2))
    print('List1 is List2 is {}.'.format(list1 is list2))

    list2[1][0] = 11  # change the reference value
    print('Warning For List1 == List2 is {}.'.format(list1 == list2))

    print('Old List2 is {}.'.format(list2))
    list2[2][3].append(4)
    print('New List2 is {}.'.format(list2))

    print('Now List1 == List2 is {}.'.format(list1 == list2))
    list2[0] = 6
    print(list1)


shallowCopy()


class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def bus():
    bus1 = Bus(['m', 'p', ' x'])
    bus2 = copy.copy(bus1)
    bus3 = copy.deepcopy(bus1)

    bus2.drop('m')
    print(bus1.passengers)
    print(id(bus1.passengers), id(bus2.passengers))

    print(id(bus3.passengers))


bus()
