class Product:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock

products = [
    Product("iPhone", 999.99, True),
    Product("AirPods", 199.99, True),
    Product("MacBook", 1299.99, False),
    Product("Charger", 49.99, True),
    Product("iPad", 499.99, False)
]

total = 0
for product in products:
    if product.in_stock:
        total += product.price

print(f"Ombordagi mahsulotlar narxi: {total}")
