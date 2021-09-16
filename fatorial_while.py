n = 1
while(True):

    n = int(input('Digite o valor de n: '))
    res = 1
    while n > 1:
        res = res * n
        n -= 1

    print(res)
