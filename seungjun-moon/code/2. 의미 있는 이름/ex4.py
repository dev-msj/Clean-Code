"""
검색하기 쉬운 이름을 사용하라
"""


def loop() -> None:
    s: int = 0
    for i in range(34):
        s += int((i * 4) / 5)

    print(s)


WORK_DAYS_PER_WEEK: int = 5
NUMBER_OF_TASK = 34


def loop_with_name() -> None:
    real_days_per_ideal_day: int = 4
    sum: int = 0

    for i in range(NUMBER_OF_TASK):
        real_task_days: int = i * real_days_per_ideal_day
        real_task_weeks: int = int(real_task_days / WORK_DAYS_PER_WEEK)
        sum += real_task_weeks

    print(sum)


if __name__ == "__main__":
    loop()
    loop_with_name()
