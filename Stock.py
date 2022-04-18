class Product:
    maker='Components'

    def __init__(self, name, price, quantity):
        self.total_price=0
        self.name=name
        self.price=int(price)
        self.quantity=int(quantity)

    def amount(self):
        self.quantity_needed = input(f'How much transistors would you like to buy?')

    def calculate(self):
        while not (int(self.quantity_needed) <= self.quantity):
            self.quantity_needed = input(f'We dont have enough, please choose another amount')

        self.total_price = int(self.quantity_needed) * self.price
        self.quantity -= int(self.quantity_needed)
        print(f'The amount you have to pay is {self.total_price} GEL')

    def __str__(self):
        return f'name: {self.name} price: {self.price} quantity: {self.quantity}'

    def __len__(self):
        return self.quantity

my_product=Product('transistor', '2', '70')
print(my_product)
print(len(my_product))
my_product.amount()
my_product.calculate()
print(f'Components left in stock: {len(my_product)} {my_product.name}s')
