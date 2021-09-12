def maximo2(num1, num2):

    if (num1 < num2):
        max = num2
    else:
        max = num1

    return max


def maximo(num1, num2, num3):

    max = maximo2(maximo2(num1, num2), num3)

    return max


def test_maximo():
    if maximo(1, 2, 3) == 3:
        print('ok for maximo(1, 2, 3)')
    else:
        print('not ok for maximo(1, 2, 3)')
    if maximo(0, -1, 1) == 1:
        print('ok for maximo(0, -1, 1)')
    else:
        print('not ok for maximo(0, -1, 1)')


test_maximo()
