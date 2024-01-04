#建立類別
class frichicken:
    def __init__(self,name,flavor,price,spice_level,parts):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.spice_level = spice_level
        self.parts = parts

#建立三個副函式
    def display_details(self):
        print(f"Chicken Name: {self.name}")
        print(f"Flavor: {self.flavor}")
        print(f"Price: ${self.price}")
        print(f"Spice Level: {self.spice_level}")
        print(f"parts: {self.parts}")
        

    def increase_spice_level(self, amount):
        self.spice_level += amount
        print(f"Spice level increased by {amount}.")

    def change_flavor(self, new_flavor):
        self.flavor = new_flavor
        print(f"Flavor changed to {new_flavor}.")

    def apply_discount(self, discount_percent):
        discount_amount = (discount_percent / 100) * self.price
        self.price -= discount_amount
        print(f"Discount applied: ${discount_amount}. New price: ${self.price}")


# 建立四個物件
chicken1 = frichicken("a","Italian_style",200,0,"Chicken wings")
chicken2 = frichicken("b","German_style",250,1,"drumstick")
chicken3 = frichicken("c","French_style",220,2,"chicken breast")
chicken4 = frichicken("d","Taiwan_style",320,3,"Chicken wings")

# 個別呼叫三個副函式
print("\n====== Chicken.1 ======")
chicken1.display_details()
chicken1.increase_spice_level(1)
chicken1.change_flavor("Barbecue")
chicken1.apply_discount(10)

print("\n====== Chicken.2 ======")
chicken2.display_details()
chicken2.increase_spice_level(2)
chicken2.change_flavor("Lemon Pepper")
chicken2.apply_discount(15)

print("\n====== Chicken.3 ======")
chicken3.display_details()
chicken3.increase_spice_level(1)
chicken3.change_flavor("Sweet Chili")
chicken3.apply_discount(5)

print("\n====== Chicken.4 ======")
chicken4.display_details()
chicken4.increase_spice_level(3)
chicken4.change_flavor("Teriyaki")
chicken4.apply_discount(20)