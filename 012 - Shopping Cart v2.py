#Shopping Cart - V2

from getpass import getpass

class Product:

    def __init__(self, prod, price, qty):
        self.__prod = prod
        self.__price = price
        self.__Qty = qty

class Cart:

    def __init__(self):
        self.__Cart = {}
        self.__Total = 0

    def addProd(self, name, price, qty): #Adding Product
        self.__Cart = {name:qty} 
        self.__Total += (price*qty)
        print('Product has been added successfully!')
    
    def showCart(self): #Verify cart
        print('Product ---- Quantity')
        result = ''
        if len(self.__Cart) > 0:
            for k,v in self.__Cart.items():
                Q = str(v)
                result = k + '-----' + Q + '\n'
        else:                
            result = 'Empty!'
        return result

    def rmProd(self, name, price, qty): #Remove product
        if name in self.__Cart:
            if qty < self.__Cart[name] and qty > 0:
                self.__Cart[name] -= qty
                self.__Total -= (price*qty)
                return 'Removed Successfully!'
            elif qty >= self.__Cart[name]:
                self.__Total -= self.__Cart[name]*price
                del self.__Cart[name]
                return 'Product Removed Successfully!'
        else:
            return 'Product not available in a Cart.'
    
    def Checkout(self, value):
        print('Total: $%.2f' %(self.__Total))
        if value < self.__Total:
            return 'Payment not confirmed. You still have items in your cart.'
        else:
            self.zeroTotal()
            self.clearCart()
            return 'Payment confirmed.'
    
    def zeroTotal(self):
        self.__Total = 0
    
    def clearCart(self):
        self.__Cart.clear()

    def showTotal(self):
        return 'Total: $ %.2f' %self.__Total

def Main():
    total = 0
    Shop = Cart()
    print('Welcome to SuperMarket\n1-Buy, 2-Remove, 3-Show Cart, 4-Total or 5-End')
    while True:
        op = input('Answer: ')
        if op == '1':
            Order = input('Product and Price(Example: Sugar 1.50 2): ').split()
            Prod = Order[0]
            Price = float(Order[1])
            Qty = int(Order[2])
            Acquired = Product(Prod, Price, Qty)
            Shop = Cart()
            Shop.addProd(Prod, Price, Qty)
            Value = float(Price)
            total += Value
        elif op == '2':
            P = input('Product to be removed: ')
            V = float(input('Price: '))
            Q = int(input('Qty: ')) 
            print(Shop.rmProd(P, V, Q))
        elif op == '3':
            print(Shop.showCart())
        elif op == '4':
            print('Payment: Money or Credit Card?')
            op = input('Answer: ')
            if op == '1':
                print(Shop.showTotal())
                value = float(input('Pay: '))
                print(Shop.Checkout(value))            
            elif op == '2':
                print(Shop.showTotal())
                CreditCard = input('Credit Card: ')
                Value = float(input('Pay: '))
                Password = getpass('Password: ')
                print(Shop.Checkout(Value))
        elif op == '5':
            print('Turn Off!')
            break

Main()
        



