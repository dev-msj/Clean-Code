"""
인코딩을 피하라

Part처럼 변수명에 범위와 변수 타입까지 있으면 해당 정보에 대한 인코딩(분석)을 해야하고 이름이 쓸데없이 길어진다.

PartRemoveEncoding에서는 __를 붙여 변수를 private으로 만들고, 타입을 명시하여 이름에서 필요없는 정보를 없앴다.
"""


class Part:
    private_str_my_name = None

    def set_name(self, name):
        self.private_str_my_name = name


class PartRemoveEncoding:
    __my_name: str = None

    def set_name(self, name):
        self.__my_name = name
