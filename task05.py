class Product:
    def __init__(self, name: str, price: float, category: str, in_stock: bool):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock


product1 = Product("Smartphone", 12999.99, "electronics", True)
product2 = Product("Headphones", 599.50, "electronics", False)

print(product1.name, "-", product1.price)
print(product2.name, "-", product2.price)
