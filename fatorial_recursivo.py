def fatorial(n):

    if(n == 0) or (n == 1):
        return 1

    return n * fatorial(n - 1)

# 0 	1
# 1 	1
# 2 	2
# 3 	6
# 4 	24
# 5 	120


print(fatorial(5))
