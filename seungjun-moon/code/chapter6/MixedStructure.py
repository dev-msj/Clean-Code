class MixedStructure:
    """
    잡종 구조의 예시
    1. {get/set}_z 함수는 private 변수를 그대로 노출한다.
    2. x, y 변수가 아무런 이유도 없이 public 변수로 구현되어 있다.
    3. x, y가 MixedStructure를 이용하는 코드들과 dependency가 발생하여 함수나 자료 구조를 추가하거나 변경하기 어려워 진다.
    """
    x: float
    y: float
    __z: float

    def set_z(self, z: float):
        self.__z = z

    def get_z(self, z: float) -> float:
        return self.__z

    def get_avg(self) -> float:
        return (self.x + self.y + self.__z) / 3
