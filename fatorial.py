n = int(input('Digite o valor de n: '))
res = n
while n > 1:
    res = res * (n - 1)
    n -= 1

if n == 0:
    res = 1

print(res)