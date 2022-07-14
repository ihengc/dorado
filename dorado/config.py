"""
@project:   dorado
@author:    ihc
@description:
"""


class BaseConfig(object):
    HOST = None
    PORT = None


class ProcedureConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    HOST = '127.0.0.1'
    PORT = 10001
