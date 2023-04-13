# Import necessary modules
import os
os.system('cls')

# Create Machine class

class Machine:

    # Create init method with resource values
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100

    # Create an order method that takes the customer's order
    # There are 3 drink options(Espresso, Latte and Cappuccino)
    # Maintainers can enter "Report" to check remaining resources
    # Mainteiners can enter "off" to turn of the machine
    # Report and Off will not be listed as options
    def order(self):
        ordering = True
        while ordering:
            drink = input("""What would you like to order?
    Espresso
    Latte
    Cappuccino\n\n""").lower()
            if drink == "espresso":
                self.espresso()
            elif drink == "latte":
                self.latte()
            elif drink == "cappuccino":
                self.cappuccino()
            elif drink == "report":
                return self.report()
            elif drink == "off":
                self.off()
                ordering = False
            else:
                input("Not a valid selection. Press enter to order again")
                os.system('cls')
    
    # Create expresso method  
    def espresso(self):
        # Check if proper resources are available
        if self.water < 50 or self.coffee < 18:
            os.system('cls')
            input("Not enough resources, contact maintenance. Press enter to return to main menu.")
            os.system('cls')
        else:
            self.water -= 50
            self.coffee -= 18
            os.system('cls')            
            input("Here is your espresso, enjoy!\nPress enter to return to main menu")
            os.system('cls')
    
    # Create latte method 
    def latte(self):
        # Check if proper resources are available
        if self.water < 200 or self.milk < 150 or self.coffee < 24:
            os.system('cls')
            input("Not enough resources, contact maintenance. Press enter to return to main menu.")
            os.system('cls')
        else:
            self.water -= 200
            self.milk -= 150
            self.coffee -= 24
            os.system('cls')
            input("Here is your latte, enjoy!\nPress enter to return to main menu")
            os.system('cls')

    # Create cappuccino method 
    def cappuccino(self):
        # Check if proper resources are available
        if self.water < 250 or self.milk < 100 or self.coffee < 24:
            os.system('cls')
            input("Not enough resources, contact maintenance. Press enter to return to main menu.")
            os.system('cls')
        else:
            self.water -= 250
            self.milk -= 100
            self.coffee -= 24
            os.system('cls')
            input("Here is your cappucino, enjoy!\nPress enter to return to main menu")
            os.system('cls')        
    
    def report(self):
        os.system('cls')
        input(f"""Resources listed below:
Water:  {self.water}ml
Milk:   {self.milk}ml
Coffee: {self.coffee}g
Press enter to return to main menu.""")
        os.system('cls')      
        self.order()
            
    def off(self):
        os.system('cls')      
        print("Machine powering down.")
    

def main():
        coffee = Machine()
        coffee.order()


if __name__ == "__main__":
    main()