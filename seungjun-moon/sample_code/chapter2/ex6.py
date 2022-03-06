"""
의미 있는 맥락을 추가하라
"""


def print_guess_statistics(candidate: str, count: int) -> None:
    number: str = ""
    verb: str = ""
    plural_modifier: str = ""

    if count == 0:
        number = "no"
        verb = "are"
        plural_modifier = "s"
    elif count == 1:
        number = "1"
        verb = "is"
    else:
        number = str(count)
        verb = "are"
        plural_modifier = "s"

    guess_message: str = f"There {verb} {number} {candidate}{plural_modifier}"

    print(guess_message)


class GuessStatisticsMessage:
    __number: str
    __verb: str
    __pluralModifier: str

    def make(self, candidate: str, count: int) -> str:
        return f"There {self.__verb} {self.__number} {candidate}{self.__pluralModifier}"

    def create_plural_dependent_message_parts(self, count: int) -> None:
        if count == 0:
            self.there_are_no_letters()
        elif count == 1:
            self.there_is_one_letter()
        else:
            self.there_are_many_letters(count)

    def there_are_many_letters(self, count: int) -> None:
        self.__number = str(count)
        self.__verb = "are"
        self.__pluralModifier = "s"

    def there_is_one_letter(self) -> None:
        self.__number = "1"
        self.__verb = "is"
        self.__pluralModifier = ""

    def there_are_no_letters(self) -> None:
        self.__number = "no"
        self.__verb = "are"
        self.__pluralModifier = "s"
