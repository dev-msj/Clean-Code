import abc


class PointBadCase:
    """
    1. 객체가 어떤 용도인지 알 수 없다.
    2. 구현을 노출한다.
    """
    x: float
    y: float


class Point(abc.ABCMeta):
    """
    1. Setter 함수명을 통해 객체가 어떤 용도인지 알 수 있다.
    2. 클래스 접근 정책을 강게한다.
    """
    __x: float
    __y: float
    __r: float
    __theta: float

    def get_x(cls) -> float:
        return cls.__x

    def get_y(cls) -> float:
        return cls.__y

    def set_cartesian(cls, x: float, y: float):
        cls.__x = x
        cls.__y = y

    def get_r(cls) -> float:
        return cls.__r

    def get_theta(cls) -> float:
        return cls.__theta

    def set_polar(cls, r: float, theta: float):
        cls.__r = r
        cls.__theta = theta
