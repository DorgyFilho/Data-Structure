#Duplicados V2 - Código mais eficiente

def duplicados(lista, n):

    #Se a lista tiver vazia
    if not lista:
        return []
    
    #Filtrar os duplicados
    repetidos = [0]*n
    copia = []
    for item in lista:
        repetidos[item] += 1
        if repetidos[item] > 1:
            copia.append(item)

    return copia

lista = [1,1,3,3,5,5,7,9,9,10,12,10,16,21,16]
print('Duplicados: ',duplicados(lista,100))

    

