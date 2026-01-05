# def my_decorator(func):
#     def wrapper():
#         print("Before function runs")
#         func()
#         print("After function runs")
#     return wrapper

# @my_decorator  # if want to check then comment this line then run code, then u will understand the work of it
# def greet():
#     print("Hello from decorator class from chaicode")

# greet()

# print(greet.__name__) # o/p = wrapper (Why wrapper?? bcz  we are returning a wrapper)




from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator  # if want to check then comment this line then run code, then u will understand the work of it
def greet():
    print("Hello from decorator class from chaicode")

greet()

print(greet.__name__)

#by using that library it's preserves the name. o/p=greet not wrap any more