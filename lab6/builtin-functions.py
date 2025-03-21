# 1

from functools import reduce
numbers = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product) 

# 2
def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    
    print(f"Uppercase Letters: {upper_count}")
    print(f"Lowercase Letters: {lower_count}")

text = input()
count_case(text)


# 3
my_input_string = input()
reversed_string = ''.join(reversed(my_input_string))
print(my_input_string == reversed_string)


# 4
import time
number = int(input("Enter a number: "))
milliseconds = int(input("Enter milliseconds: "))
time.sleep(milliseconds / 1000)
print("Square root of", number,  "after", milliseconds, "milliseconds is", pow(number, 0.5))


# 5
from functools import reduce
from operator import mul
import time
import math
def true(elements):
    return all(elements)

print(true((True, True, True)))
print(true((True, False, True)))