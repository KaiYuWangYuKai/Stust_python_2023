#員工類別
class Employee:
    def __init__(self, name, years_of_service, hours_worked):
        self.name = name
        self.years_of_service = years_of_service
        self.hours_worked = hours_worked
    #回傳名字
    def query_name(self):
        return self.name
    #回傳年資
    def calculate_years_of_service(self):
        return self.years_of_service
    #回傳工時
    def calculate_hours_worked(self):
        return self.hours_worked
    #計算月薪
    def calculate_monthly_salary(self, hourly_rate):
        return self.hours_worked * hourly_rate
    #增加工時
    def increase_hours_worked(self, additional_hours):
        self.hours_worked += additional_hours
    #增加年資
    def increase_years_of_service(self, additional_years):
        self.years_of_service += additional_years

#飲料類別
class Beverage:
    def __init__(self, name, sweetness,price):
        self.name = name
        self.sweetness = sweetness
        self.price = price
    #修改飲料名稱
    def modify_name(self, new_name):
        self.name = new_name
    #調整甜度
    def adjust_sweetness(self, new_sweetness):
        self.sweetness = new_sweetness
    #調整價錢
    def adjust_price(self, new_price):
        self.price = new_price

#熱飲(繼承飲料)
class HotBeverage(Beverage):
    def __init__(self, name, sweetness, temperature,price):
        super().__init__(name, sweetness,price)
        self.temperature = temperature
#冷飲(繼承飲料)
class ColdBeverage(Beverage):
    def __init__(self, name, sweetness, ice_level,price):
        super().__init__(name, sweetness,price)
        self.ice_level = ice_level

# 建立員工物件
employee1 = Employee("John Doe", 5, 160)
#顯示員工資訊
print("Employee Details:")
print("Name:", employee1.query_name())
print("Years of Service:", employee1.calculate_years_of_service())
print("Hours Worked:", employee1.calculate_hours_worked())
print("Monthly Salary:", employee1.calculate_monthly_salary(10.0))
#增加員工工時
employee1.increase_hours_worked(10)
#增加員工年資
employee1.increase_years_of_service(1)
#顯示調整後的資訊(加完後的工時、年資)
print("Updated Hours Worked:", employee1.calculate_hours_worked())
print("Updated Years of Service:", employee1.calculate_years_of_service())

# 建立飲料物件
hot_coffee = HotBeverage("Coffee", "Medium", "Hot",50)
cold_tea = ColdBeverage("Tea", "Sweet", "Extra Ice",30)
#顯示飲料相關資訊
print("\nBeverage Details:")
print(f"Hot Coffee: {hot_coffee.name}, Sweetness: {hot_coffee.sweetness}, Temperature: {hot_coffee.temperature}")
print(f"Cold Tea: {cold_tea.name}, Sweetness: {cold_tea.sweetness}, Ice Level: {cold_tea.ice_level}")

#修改飲料名稱，調整甜度，調整價錢
hot_coffee.modify_name("Latte")
cold_tea.adjust_sweetness("Less Sweet")
hot_coffee.adjust_price(100)

#顯示飲料修改後的相關資訊
print("\nAfter Modification:")
print(f"Hot Coffee: {hot_coffee.name}, Sweetness: {hot_coffee.sweetness}, Price: ${hot_coffee.price}")
print(f"Cold Tea: {cold_tea.name}, Sweetness: {cold_tea.sweetness}, Price: ${cold_tea.price}")