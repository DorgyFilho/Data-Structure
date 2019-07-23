#Inverter

def inverter(lista):

    #Se não for lista ou se tiver vazia
    if not lista:
        return []
    
    inicio = 0
    fim = len(lista)-1
    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1
    return lista

print(inverter([1,2,3,4,5,6]))
    