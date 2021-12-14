def busca(lista, elemento):

    for idx, e in enumerate(lista):
        if(e == elemento):
            return idx

    return False


print(busca(['a', 'e', 'i'], 'e'))
# deve devolver => 1

print(busca([12, 13, 14], 15))
# deve devolver => False
