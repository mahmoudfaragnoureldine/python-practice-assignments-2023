# --------------------
# -- Function Scope --
# --------------------

x = 1  # Global Scope
# اقدر اوصله من اى مكان فى الدنيا


def first():
    global x
    x = 2
    print(f"print x from function(first) scope: {x}")


def second():
    x = 3
    print(f"Print x from function(second) scope: {x}")


# print(f"Print x from global scope: {x}")  # Print x from global scope: 1
first()  # print x from function(first) scope: 2
second()  # Print x from function(second) scope: 3
print(f"Print x from global scope: {x}")  # Print x from global scope: 2
