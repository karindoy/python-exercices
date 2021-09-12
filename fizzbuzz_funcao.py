def fizzbuzz(n):

    if (n % 3 == 0):
        res = 'Fizz'
    elif(n % 5 == 0):
        res = 'Buzz'

    if (n % 3 == 0) & (n % 5 == 0):
        res = 'FizzBuzz'
    if (n % 3 != 0) & (n % 5 != 0):
        res = n

    return res


def test_fizzbuzz():
    if fizzbuzz(3) == 'Fizz':
        print('ok for fizzbuzz(3)')
    else:
        print('not ok for fizzbuzz(3)')

    if fizzbuzz(5) == 'Buzz':
        print('ok for fizzbuzz(5)')
    else:
        print('not ok for fizzbuzz(5)')

    if fizzbuzz(15) == 'FizzBuzz':
        print('ok for fizzbuzz(15)')
    else:
        print('not ok for fizzbuzz(15)')


test_fizzbuzz()
