
class Product:
    def __init__(self, name, price, number_of_products):
        self.name = name
        self.price = price
        self.number_of_products = number_of_products

class Inventory:
    def __init__(self):
        self.products = []

    def show_inventory_options(self):
        print("\n===== Inventario =====\n")
        print("1. Agregar un producto")
        print("2. Mostrar todos los productos")
        print("3. Calcular el valor total del inventario")
        print("0. Exit")

    def get_inventory_option(self):
        while True:
            try:
                answer = int(input("Seleccione una opción en el Menu: \n"))
                if 0 <= answer <= 3:
                    return answer
                print("Opción invalida.  (Usa 0 ... 3.)")
            except ValueError:
                print("Ingrese solo números.")
        
    def add_product(self):
        name = input("Digite el nombre del producto: ")
        price = int(input("Digite el precio del producto: "))
        number_products = int(input("Digite cuantas unidades del producto: "))
        my_product = Product(name,price,number_products)
        self.products.append(my_product) 
        print(f"Producto agregado!")

    def show_products(self):
        for product in self.products:
            print(f"Producto: {product.name}")
            print(f"Precio: {product.price}")
            print(f"Cantidad: {product.number_of_products}")
            print()

    def calculate_total_value(self):
        total = 0

        for product in self.products:
            total += product.price * product.number_of_products

        return total


def main():
    inventory = Inventory()

    while(True):
        inventory.show_inventory_options()
        answer = inventory.get_inventory_option()
        match answer:
            case 1:
                inventory.add_product()
            case 2:
                inventory.show_products()
            case 3:
                print(f"Valor total del inventario: {inventory.calculate_total_value()}")
            case 0:
                break
    

if __name__ == "__main__":
    main()