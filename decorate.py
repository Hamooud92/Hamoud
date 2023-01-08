def cool(some_def_func):
    def super_cool():
        return 'i am super cool'
    return super_cool()


def hello(name):
    print("your name is "+name)

print(cool(hello('hamoud')))


def new_decorator(orginal_finction):
    def wrap_func():
        print('etra code')
        orginal_finction()
        print("some after the orginal")
    return  wrap_func()

def func_needs():
    print("i need to be decorated")

dd=new_decorator(func_needs)
@new_decorator
def func_needs():
    print("i need to be decorated")



