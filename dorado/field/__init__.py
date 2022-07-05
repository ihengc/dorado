"""
@project:   dorado
@author:    ihc
@description:
"""

__all__ = ['TinyintField', 'SmallintField', 'MediumintField', 'BigintField', 'BaseField']


class BaseField:
    def __init__(self, name, autoIncrement=False, primaryKey=False, unique=False, default=None, comment=""):
        self.name = name
        self.autoIncrement = autoIncrement
        self.primaryKey = primaryKey
        self.unique = unique
        self.default = default
        self.comment = comment
        self.kindName = None

    # def __str__(self):
    #     return self.kindName
    #
    # def __repr__(self):
    #     return self.kindName


class TinyintField(BaseField):
    def __init__(self, name, autoIncrement=False, primaryKey=False, unique=False, default=None, comment=""):
        super(TinyintField, self).__init__(
            name,
            autoIncrement,
            primaryKey,
            unique,
            default,
            comment,
        )
        self.kindName = "TINYINT"


class SmallintField(BaseField):
    def __init__(self, name, autoIncrement=False, primaryKey=False, unique=False, default=None, comment=""):
        super(SmallintField, self).__init__(
            name,
            autoIncrement,
            primaryKey,
            unique,
            default,
            comment,
        )
        self.kindName = "SMALLINT"


class MediumintField(BaseField):
    def __init__(self, name, autoIncrement=False, primaryKey=False, unique=False, default=None, comment=""):
        super(MediumintField, self).__init__(
            name,
            autoIncrement,
            primaryKey,
            unique,
            default,
            comment,
        )
        self.kindName = "MEDIUMINT"


class BigintField(BaseField):
    def __init__(self, name, autoIncrement=False, primaryKey=False, unique=False, default=None, comment=""):
        super(BigintField, self).__init__(
            name,
            autoIncrement,
            primaryKey,
            unique,
            default,
            comment,
        )
        self.kindName = "BIGINT"


class VarcharField(BaseField):
    def __init__(self, name, length, autoIncrement=False, primaryKey=False, unique=False, default=None, comment=""):
        super(VarcharField, self).__init__(
            name,
            autoIncrement,
            primaryKey,
            unique,
            default,
            comment,
        )
        self.length = length
        self.kindName = "VARCHAR(%s)" % str(length)
