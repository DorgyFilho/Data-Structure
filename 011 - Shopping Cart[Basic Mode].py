#Shopping Cart - Basic Mode

class Product:

    def __init__(self, prod, price):
        self.__prod = prod
        self.__price = price

class Cart:

    def __init__(self):
        self.__Cart = []
        self.__Total = 0
   
    def addProd(self, new): #Adding Product
        self.__Cart.append(new)
        print('Product has been added successfully!')
    
    def showCart(self): #Verify cart
        if len(self.__Cart) > 0:
            return True #There is/are products
        else:
            return False #There isn't/aren't products
    
    def rmProd(self, prod): #Cear the cart
        self.__Cart.remove(prod)
        print('Product has been removed successfully!')

    def TotalPrice(self, value): #Total Value
        self.__Total = value
        return 'Total: $ %.2f' %self.__Total    

def Main():
    total = 0
    Shop = Cart()
    print('Welcome to SuperMarket\n1-Buy, 2-Remove, 3-Show Cart, 4-Total or 5-End')
    while True:
        op = input('Answer: ')
        if op == '1':
            Order = input('Product and Price(Example: Sugar 1.50): ').split()
            Prod = Order[0]
            Price = float(Order[1])
            Acquired = Product(Prod, Price)
            Shop = Cart()
            Shop.addProd(Acquired)
            Value = float(Price)
            total += Value
        elif op == '2':
            Shop.rmProd(Acquired)
            total = 0
        elif op == '3':
            print(Shop.showCart())
        elif op == '4':
            print(Shop.TotalPrice(total))
        elif op == '5':
            print('Turn Off!')
            break

Main()
        



