class Car:


    def __init__(self,brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
    
    def info(self) -> str:
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year})"

c01 = Car('GM', 'Cobalt', 2020)
c02 = Car('GM', 'Nexia',2012)


print(c01.info())
print(c02.info())
