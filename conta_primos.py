def verificarPrimalidade(n):
    i = 1
    isPrime = True
    while (n > i) & (isPrime == True):
        if (n % i == 0) & (i != 1):
            isPrime = False
        i += 1

    return isPrime


def n_primos(n):
    countPrime = 0
    while (n > 1):

        if (verificarPrimalidade(n)):
            countPrime += 1
        n -= 1

    return countPrime


def test_n_primos():
    if n_primos(2) == 1:
        print('ok for n_primos(2)')
    else:
        print('not ok for n_primos(2)')

    if n_primos(4) == 2:
        print('ok for n_primos(4)')
    else:
        print('not ok for n_primos(4)')

    if n_primos(121) == 30:
        print('ok for n_primos(121)')
    else:
        print('not ok for n_primos(121)')


test_n_primos()
