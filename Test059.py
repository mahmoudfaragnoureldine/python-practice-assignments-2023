# ---------------------------------
# -- Function Default Parameters --
# ---------------------------------

# دا معناه انك بحط قيمه افتراضيه للبراميتر اللى عندك فى الفنكشن

# لازم الديفولت براميتر يكون اخر حاجه فى الفنكشن بتاعتك


def say_hello(name, age="Unknown", country="Unknown"):
    print(f"hello {name} your age is {age} and your country is {country}")


say_hello("Walid", 22, "Egypt")
say_hello("Ahmed", 25)
say_hello("Mohammed")
