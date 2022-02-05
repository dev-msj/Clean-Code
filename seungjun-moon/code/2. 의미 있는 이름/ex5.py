"""
인코딩을 피하라
"""


class Part:
    __m_dsc: str

    def set_name(self, name):
        self.__m_dsc = name


class PartRemovePrefix:
    __name: str

    def set_name(self, name):
        self.__name = name
