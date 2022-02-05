"""
의미 있게 구분하라
"""


def copy_str(a1: str, a2: str) -> None:
    a2 = a1


def copy_str_rename(source: str, destination: str) -> None:
    """
    인수명을 의미있게 만들어주면 코드 읽기가 훨씬 쉬워진다.
    """
    destination = source


if __name__ == "__main__":
    copy_str()
    copy_str_rename()
