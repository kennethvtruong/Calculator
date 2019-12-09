class Calculator:
    def __init__(self, num1: float, num2: float, operator: str):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
    def get_numbers(self):
        self.num1 = float(input("What's the first number? "))
        self.num2 = float(input("What's the second number? "))
        self.operator = str(input("What would you like to do? "))
    def addition(self):
        sum_of_nums = self.num1 + self.num2
        return sum_of_nums
    def subtraction(self):
        difference_of_nums = self.num1 - self.num2
        return difference_of_nums
    def multiplication(self):
        product_of_nums = self.num1 * self.num2
        return product_of_nums
    def division(self):
        quotient_of_nums = self.num1 / self.num2
        if self.num2 == "0":
            print("That ain't it, chief")
        return quotient_of_nums
    def choose_operator(self):
        if self.operator == "+":
            print(my_calc.addition())
        if self.operator == "-":
            print(my_calc.subtraction())
        if self.operator == "*":
            print(my_calc.multiplication())
        if self.operator == "/":
            print(my_calc.division())
        else:
            print("Bro, can you just like an actual operator")
            my_calc.get_numbers()
            my_calc.choose_operator()
            quit()



my_calc = Calculator(4,3,"+")
my_calc.get_numbers()
my_calc.choose_operator()

