# ---------------------------------------
# -- Function Parameters and Arguments --
# ---------------------------------------

# a, b, c = "Walid", "Ahmed", "Sayed"

# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")

# def                       => Function Keyword [Define]
# say_hello                 => Function Name
# Name                      => Parameter
# print(f"Hello {name}")    => Task
# say_hello("Walid")        => Walid is The Argument


# def say_hello(name):
#   print(f"Hello {name}")


# say_hello("Walid")
# say_hello(a)
# say_hello(b)
# say_hello(c)


def addition(n1, n2):
    if type(n1) != int or type(n2) != int:
        print("Only Integers Allowed")

    else:
        print(n1 + n2)


addition(-60, 100)


def fullname(first, middle, last):
    print(
        f"Hello {first.strip().capitalize()} {middle.strip().capitalize():.1s} {last.strip().capitalize()}"
    )


fullname("Walid", "farag", "noureldinne")
