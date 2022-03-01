import abc


class VehicleBadCase(abc.ABCMeta):
    """
    Getter 함수가 너무 많은 정보를 알려주고 있다.
    """
    __tank_capacity: float
    __gallons: float

    def get_fuel_tank_capacity_gallons(cls) -> float:
        return cls.__tank_capacity

    def get_gallons_of_gasoline(cls) -> float:
        return cls.__gallons


class Vehicle(abc.ABCMeta):
    """
    Getter 함수가 자동차 연료 상태를 백분율이라는 추상적인 개념으로 알려준다.
    """
    __tank_capacity: float
    __gallons: float

    def __get_percent_fuel_remaining(cls) -> float:
        return (cls.__gallons / cls.__tank_capacity) * 100
