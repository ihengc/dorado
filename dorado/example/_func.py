"""
@project:   dorado
@author:    ihc
@description:
"""


class TwilightBus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)


class HauntedBus:

    def __init__(self, passengers=[]):  # 使用可变类型作为函数参数
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


def hauntedBus():
    bus1 = HauntedBus(['Alice', 'Bill'])
    print(bus1.passengers)

    bus1.pick('Charlie')
    bus1.drop('Alice')
    print(bus1.passengers)

    bus2 = HauntedBus()
    bus2.pick('Carrie')
    print(bus2.passengers)

    bus3 = HauntedBus()
    print(bus3.passengers)  # 会有值在列表中

    bus3.pick('Dave')
    print(bus2.passengers)  # bus2和bus3共用一个list
    print(bus3.passengers is bus2.passengers)  # True

    # print(dir(HauntedBus.__init__))
    print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)


hauntedBus()
