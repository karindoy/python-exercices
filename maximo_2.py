def maximo(num1, num2):

    if (num1 < num2):
        max = num2
    else:
        max = num1

    return max


def test_maximo():
    if maximo(1, 2) == 2:
        print('ok for maximo(1, 2)')
    else:
        print('not ok for maximo(1, 2)')
    if maximo(2, 1) == 2:
        print('ok for maximo(2, 1)')
    else:
        print('not ok for maximo(2, 1)')


test_maximo()
