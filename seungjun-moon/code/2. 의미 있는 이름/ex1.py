from typing import List

'''
의도를 분명히 밝혀라.
'''


def create_variable():
    """
    이름을 의미 있게 지어주면 변수명만 봐도 의도를 파악할 수 있다.
    """
    elapsedTimeInDays: int
    daysSinceCreation: int
    daysSinceModification: int
    fileAgeInDays: int


# 의미있는 이름을 활용해 코드를 개선1
def get_them() -> List[List[int]]:
    """
    복잡한 문장은 없지만 코드가 하는 일을 짐작할 수 없다.
    """
    list1: List[List[int]] = []
    the_list: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    for x in the_list:
        if x[0] == 4:
            list1.append(x)

    return list1


# 의미있는 이름을 활용해 코드를 개선2
STATUS_VALUE = 0
FLAGGED = 4


def get_flagged_cells() -> List[List[int]]:
    """
    변수명을 의미있게 지어주면 코드가 더 명확해진다.
    """
    flagged_cells: List[List[int]] = []
    game_board: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    for x in game_board:
        if x[STATUS_VALUE] == FLAGGED:
            flagged_cells.append(x)

    return flagged_cells


# 의미있는 이름을 활용해 코드를 개선3
class Cell:
    cell: List[int]

    def __init__(self, cell: List[int] = None):
        self.cell = [] if cell is None else cell

    def is_flagged(self) -> bool:
        return True if self.cell[STATUS_VALUE] == FLAGGED else False


def get_flagged_cells_with_class() -> List[Cell]:
    """
    List[int]를 Cell Class로 대체하고
    is_flagged 함수를 활용하여 상수를 감춰준다.
    """
    flagged_cells: List[Cell] = []
    game_board: List[Cell] = []
    for cell_data in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
        game_board.append(Cell(cell_data))

    for cell in game_board:
        if cell.is_flagged():
            flagged_cells.append(cell)

    return flagged_cells


if __name__ == "__main__":
    create_variable()
    print(get_them())
    print(get_flagged_cells())
    for cell_obj in get_flagged_cells_with_class():
        print(cell_obj.cell)
