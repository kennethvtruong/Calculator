class Calculator:
    def __init__(self, num1: str, num2: str, operator: str):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
    def get_numbers(self):
        self.num1 = (input("What's the first number? "))
        if not self.num1.isalnum():
            print("That is not a number, idiot, try again")
            my_calc.get_numbers()
            my_calc.choose_operator()
            quit()
        else:
            float(self.num1)
        self.num2 = (input("What's the second number? "))
        if not self.num2.isalnum():
            print("That is not a number, idiot, try again")
            my_calc.get_numbers()
            my_calc.choose_operator()
            quit()
        else:
            float(self.num2)
    def addition(self):
        sum_of_nums = float(self.num1) + float(self.num2)
        return sum_of_nums
    def subtraction(self):
        difference_of_nums = float(self.num1) - float(self.num2)
        return difference_of_nums
    def multiplication(self):
        product_of_nums = float(self.num1) * float(self.num2)
        return product_of_nums
    def division(self):
        if self.num2 == "0":
            print("Bro, you know that ain't gon work")
            my_calc.get_numbers()
            my_calc.choose_operator()
        else:
            quotient_of_nums = float(self.num1) / float(self.num2)
            return quotient_of_nums
    def choose_operator(self):
        self.operator = (input("What would you like to do? "))
        if self.operator == "+":
            print(my_calc.addition())
            quit()
        if self.operator == "-":
            print(my_calc.subtraction())
            quit()
        if self.operator == "*":
            print(my_calc.multiplication())
            quit()
        if self.operator == "/":
            print(my_calc.division())
            quit()
        else:
            print("Bro, can you just like, choose an actual operator. Try again")
            my_calc.get_numbers()
            my_calc.choose_operator()
            quit()
my_calc = Calculator(4.0 , 3.0 , "+")
my_calc.get_numbers()
my_calc.choose_operator()
