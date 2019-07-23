#Encontrar números duplicados

def duplicados(lista, n):

    #Se a lista tiver vazia...
    if not lista:
        return []
    
    #Processo de filtro...
    copia = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                copia.append(lista[j])
    
    return copia


lista = [1,1,3,3,5,9,100,92,63,100,52,81,52]
while True:
    num = input('Digite um número: ')
    if num == 'fim':
        break
    else:
        try:
            num = int(num)
            print(duplicados(lista, num))
        except:
            print('Inválido!')

