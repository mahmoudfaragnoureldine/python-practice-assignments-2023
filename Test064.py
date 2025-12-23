# ------------------------
# -- Function => Lambda --
# -- Anonymous Function --
# ------------------------
# [1] It has no name
# [2] You can call it inline without Defining it
# [3] You can use it in return data from another function
# [4] Lambda used for simple function and Def handle the large tasks
# [5] Lambda is one single expression not block of code
# [6] lambda type is function
# ------------------------------------

# فنكشن مجهوله معرفش عنها اى حاجه


def say_hello(name, age): return f"Hello {name} your age is: {age}"

hello = lambda name, age : f"Hello {name} your age is: {age}"

print(say_hello("Ahmed", 36))
print(hello("ahmed", 36)) 

print(say_hello.__name__)  # say_hello
print(hello.__name__)      # <lambda>

print(type(hello))         # <class 'function'>

