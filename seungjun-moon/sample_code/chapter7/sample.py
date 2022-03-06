def a():
    print('a')
    b()


def b():
    print('b')
    c()


def c():
    print('c')
    d()


def d():
    raise Exception('Exception!')


if __name__ == "__main__":
    try:
        a()
    except Exception as e:
        print(e)
