n = int(input('Digite o valor de n: '))
k = int(input('Digite o valor de k: '))


def fatorial(f):
    res = 1
    while f > 1:
        res = res * f
        f -= 1

    return res


coeficienteBinomial = fatorial(n) / (fatorial(k) * fatorial(n - k))
print(coeficienteBinomial)
