#Move Zeros

def moveZero(lista):
    vetor = 0 #Quantidade de vezes que os zeros são movimentados na lista.
    for pos, num in enumerate(lista):
        if num != 0:
            lista[vetor], lista[pos] = lista[pos], lista[vetor]
            vetor += 1
        print('Processo %s: %s' %(str(pos), str(lista)))
    return 'Lista Final: %s' %lista


print(moveZero([0,1,5,0,2,7]))