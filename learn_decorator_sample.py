__author__ = 'vinayak'

#calling the method directly
def print_number(num):
    print("number:", num)

print_number(18)

#using the inner function concept defining decorator
def inner_printing_tag(func):
    def inner_func(x):
        print("Pre-processing")
        func(x)
        print("post-procssing")
    return inner_func


print_number = inner_printing_tag(print_number)
print_number(11)

#using the decorator tag

@inner_printing_tag
def print_numbers(num):
    print("number:", num)

print_numbers(94)
