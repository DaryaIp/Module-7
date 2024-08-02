
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""
    def add(self, *products):
        existing_products = self.get_products().strip().split('\n') #Не знаю перебирают ли так строки
        product_names = {line.split(',')[0].strip() for line in existing_products}

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in product_names:
                    file.write(f"{product}\n")
                    product_names.add(product.name)
                else:
                    print(f'Продукт {product.name} уже есть в магазине')

        # Закрытие файла
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
