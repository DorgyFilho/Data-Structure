#Fatorial

def Fatorial(n):
    if n <= 1:
        return 1
    else:
        return n*Fatorial(n-1)
num = int(input('Digite um número: '))
Resultado = Fatorial(num)
print(Resultado)
