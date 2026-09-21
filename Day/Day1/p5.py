# concept: decorator is a python feature that lets you to modify the behaviour of a function using @ symbol
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
@my_decorator
def say_hello():
    print("Hello !")

say_hello()