import time

def factorial(n):
    """Calculate the factorial of a given number n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sum_factorial():
    """Calculate the sum of the first 50 factorials."""
    # Using a local list instead of a global variable
    factorial_list = [factorial(i) for i in range(50)]
    result = sum(factorial_list)
    
    print("Final SUM = {}".format(result))
    return result

if _name_ == "_main_":
    sum_factorial()