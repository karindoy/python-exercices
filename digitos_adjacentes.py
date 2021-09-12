n = input('Digite um número inteiro: ')
lenghtN = len(n)
isEqualToAdjacent = False
n = int(n)

leftNum = -10
rightNum = -10

i = 0
if lenghtN != 1 :
    while ( i < lenghtN) & (isEqualToAdjacent == False )  :
        
        actualNumber =  n % 10 
        n = n // 10
        leftNum =  n % 10 

        if (actualNumber == rightNum) |  (actualNumber == leftNum):
            isEqualToAdjacent = True

        rightNum = actualNumber

        i+=1
else:
    isEqualToAdjacent = False

if isEqualToAdjacent == True:
    print('sim')
else:
    print('não')    