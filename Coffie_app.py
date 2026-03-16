class Coffie:

    # Initialize coffie with name and price

    def __init__(self,name,price):
        self.name = name
        self.price = price

class Order:
    
    # Initialize order with empty list

    def __init__(self):
        self.items=[]

    # Add coffie to items

    def add_item(self,coffie):
        self.items.append(coffie)

        print(f"Added {coffie.name} to your order.")

    def total(self):
        return sum(item.price for item in self.items)
    
    # Show orders summary

    def show_order(self):

        if not self.items:
            print("No items in order.")

            return 
        
        print("\nYour order:")

        for i,item in enumerate(self.items,1):
            print(f"{i}. {item.name}-${item.price}")

        print(f"Total: ${self.total()}\n")

    # Handle checkout process

    def checkout(self):
        if not self.items:
            print("Your cart is empty.")

            return 
        
        self.show_order()

        conform = input("Proceed to checkout? (yes\no):").strip().lower()

        if conform == 'yes':
            print("Order conformed! Thank you.")

            self.items.clear()
        
        else:
            print("Checkout cancelled.")

def main():
    menu = [
        Coffie("Espressp", 2.5),
        Coffie("Latte", 3.5),
        Coffie("Cappuccino", 3.0),
        Coffie("Americano", 2.0),

    ]
    order = Order()

    # User interaction

    while True:
        print("***COFFIE MENU***")

        for i, coffie in enumerate(menu, 1):
            print(f"{i}. {coffie.name} - ${coffie.price}")
        print("5. View order")
        print("6. Checkout")
        print("7. Exit")

        choice = int(input("Choose an option: "))

        if choice in [1,2,3,4]:
            order.add_item(menu[int(choice)-1])
        elif choice == 5:
            order.show_order()
        elif choice == 6:
            order.checkout()
        elif choice == 7:
            break
        else: 
            print("Invalid choice. Try again,")

if __name__ == "__main__":
    main()