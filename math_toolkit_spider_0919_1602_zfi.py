# 代码生成时间: 2025-09-19 16:02:37
import scrapy
def add(a, b):
    '''
    Add two numbers
    :param a: First number
    :param b: Second number
    :return: Sum of the two numbers
    '''
    return a + b
def subtract(a, b):
    '''
    Subtract second number from the first
    :param a: First number
    :param b: Second number
    :return: Difference of the two numbers
    '''
def multiply(a, b):
    '''
    Multiply two numbers
    :param a: First number
    :param b: Second number
    :return: Product of the two numbers
    '''
def divide(a, b):
    '''
    Divide first number by the second
    :param a: First number
    :param b: Second number
    :return: Quotient of the two numbers
    :raises: ZeroDivisionError if b is zero
    '''
def power(a, b):
    '''
    Raise the first number to the power of the second
    :param a: Base number
    :param b: Exponent
    :return: Result of raising a to the power of b
    '''
def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        sum = add(num1, num2)
        print(f"Sum: {sum}")
        diff = subtract(num1, num2)
        print(f"Difference: {diff}")
        product = multiply(num1, num2)
        print(f"Product: {product}")
        quotient = divide(num1, num2)
        print(f"Quotient: {quotient}")
        power_result = power(num1, num2)
        print(f"Power: {power_result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
def run_from_spider():
    # This function will be called from Scrapy spider
    pass
def run_spider(math_toolkit_spider):
    # This function will run Scrapy spider
    pass
def __str__(self):
    return "MathToolkitSpider"
def __init__(self):
    self.math_toolkit = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'power': power
    }

class MathToolkitSpider(scrapy.Spider):
    name = 'math_toolkit'
    def __init__(self, *args, **kwargs):
        super(MathToolkitSpider, self).__init__(*args, **kwargs)
        self.math_toolkit = {
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide,
            'power': power
        }
    def start_requests(self):
        yield scrapy.Request(url='http://example.com')
    def parse(self, response):
        pass

if __name__ == '__main__':
    main()