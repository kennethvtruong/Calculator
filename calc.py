class Calculator:
    def __init__(self, num1, num2, ):
        self.num1 = num1
        self.num2 = num2
    def get_numbers(self):
        self.num1 = int(input("What's the first number?" ))
        self.num2 = int(input("What's the second number?" ))
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
        return quotient_of_nums



my_calc = Calculator(5,5)
my_calc.get_numbers()
print(my_calc.multiplication())
