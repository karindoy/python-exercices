
def is_prime(n):

    x = n
    isPrime = True
    while (x > 1):

        if (x != n) and (x != 1) and (n % x == 0):
            isPrime = False
        x -= 1

    return isPrime


def maior_primo(n):

    i = 1
    highestPrime = i
    while(i <= n):
        if is_prime(i):
            highestPrime = i

        i += 1
    return highestPrime


def test_is_prime():
    if is_prime(100) == False:
        print('ok for is_prime(100)')
    else:
        print('not ok for is_prime(100)')
    if is_prime(97) == True:
        print('ok for is_prime(97)')
    else:
        print('not ok for is_prime(97)')


test_is_prime()


def test_highest_prime():
    if maior_primo(100) == 97:
        print('ok for maior_primo(100)')
    else:
        print('not ok for maior_primo(100)')
    if maior_primo(7) == 7:
        print('ok for maior_primo(7)')
    else:
        print('not ok for maior_primo(7)')


test_highest_prime()
