"""
@project:   dorado
@author:    ihc
@description:
"""


def noCopy():
    a = [1, 2, 3]
    b = a
    b.append(4)
    print("No copy for reference:{}.".format(a is b))


noCopy()


def dictExample():
    charles = {'name': 'Charles L. Dodgson', 'born': 1832}
    lewis = charles
    print('Lewis is charles:{}.'.format(lewis == charles))
    lewis['balance'] = 950
    print('Charles balance is {}.'.format(charles['balance']))
    alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
    print('Charles == Alex is {}.'.format(alex == charles))
    print('Charles is not Alex is {}.'.format(alex is not charles))


dictExample()
