#Algumas funções matemáticas

def Fatorial(num):
    if num <= 1:
        return 1
    else:
        return num*Fatorial(num-1)

def Potencia(b,e):
    if e == 0:
        return 1
    else:
        return b * Potencia(b, e-1)

def Fibonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)


    

