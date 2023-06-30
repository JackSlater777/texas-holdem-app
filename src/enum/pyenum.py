from enum import IntEnum


class PyEnum(IntEnum):
    @classmethod
    def name_list(cls):
        return list(map(lambda c: c.name, cls))

    @classmethod
    def value_list(cls):
        return list(map(lambda c: c.value, cls))
