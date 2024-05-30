#oppgavesett 3 oppgave 2

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        if isinstance(other, Product):
            return Product(f'{self.name} + {other.name}', self.price + other.price)
        else:
            raise TypeError('Only Products can be added to a Product')

    def __str__(self):
        return f'{self.name} - Price: {self.price: .2f}'

produkt1 = Product('Banana ', 5.00)
produkt2 = Product('Vannmelon', 50.00)

kombiner = produkt1 + produkt2
print(kombiner)
