def soma_hipotenusas(n):

    i = 1
    somaHipotenusa = 0

    while i <= n:
        if(é_hipotenusa(i)):
            somaHipotenusa = somaHipotenusa + i
        i += 1
    return somaHipotenusa


def é_hipotenusa(n):

    i = j = 1

    while i < n:

        while j < n:
            if ((n ** 2) == (i ** 2) + (j ** 2)):
                return True

            j += 1

        i += 1
        j = 1

    return False


é_hipotenusa(5)


def test_é_hipotenusa():
    if é_hipotenusa(5) == True:
        print('ok for é_hipotenusa(5)')
    else:
        print('not ok for é_hipotenusa(5)')

    if é_hipotenusa(3) == False:
        print('ok for é_hipotenusa(3)')
    else:
        print('not ok for é_hipotenusa(3)')

    if é_hipotenusa(13) == True:
        print('ok for é_hipotenusa(13)')
    else:
        print('not ok for é_hipotenusa(13)')


def test_soma_hipotenusas():
    if soma_hipotenusas(25) == 105:
        print('ok for soma_hipotenusas(25)')
    else:
        print('not ok for soma_hipotenusas(25)')


test_é_hipotenusa()
test_soma_hipotenusas()
