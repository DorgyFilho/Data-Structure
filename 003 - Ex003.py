#Potenciação

# Ineficiente

# def pot(b,p):
#     if p == 0:
#         return 1
#     else:
#         return b*pot(b,p-1)

# print(pot(2,5))

#Eficiente
def pot(b,p):
    if p == 0:
        return 1
    else:
        resultado = b ** p
        return resultado

print(pot(2,5))
