#Pilha de Pratos

class Pilha():

    #Construtor
    def __init__(self):
        self.pilha = []
    
    #Adicionar prato
    def add(self, novo):
        self.pilha.append(novo)
    
    #Remover Prato
    def remover(self):
        if not self.verificar():
            self.pilha.pop(len(self.pilha)-1)
    
    def topo(self):
        if not self.verificar():
            return self.pilha[-1]
        else:
            return None
    
    #Verificar pilha
    def verificar(self):
        if len(self.pilha) == 0:
            return True #Lista vazia
        else:
            return False #Pilha existente
    
    def verLista(self):
        return self.pilha
    
    def tamanho(self):
        return len(self.pilha)

def main():

    Teste = Pilha()

    while True:
        #Controlar o programa a partir deste menu.
        print('Escolha uma opção:\n1-Add\n2-Remover\n3-Verificar\n4-Ver Pilha\n5-Ver Topo\n6-Tamanho da Lista\n7-Sair')
        op = input('Digite a sua opção: ')
        if op == '1':
            item = input('Digite um item: ')
            Teste.add(item)
        elif op == '2':
            Teste.remover()
        elif op == '3':
            print(Teste.verificar())
        elif op == '4':
            print(Teste.verLista())
        elif op == '5':
            print(Teste.topo())
        elif op == '6':
            print(Teste.tamanho())
        elif op == '7':
            print('Encerrado!')
            break    

main()
