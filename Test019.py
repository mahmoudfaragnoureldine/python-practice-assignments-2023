# -------------
# -- Numbers --
# -------------

# Integer الرقم العادى سواء موجب او سالب او صفر
print(type(1))
print(type(100))
print(type(-10))
print(type(-110))

# Float اى رقم فيه علامه عشريه
print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))

# Complex 
myComplexNumber = 5+6j

print(type(myComplexNumber))

print("my real part is: {}".format(myComplexNumber.real))
print("my imaginary part is: {}".format(myComplexNumber.imag))


# [1] you can convert from Int to Float or Complex
# [2] you can convert from Float to int or complex
# [3] you cannot convert complex to any type

print(100)
print(float(100))
print(complex(100))

print(1.50)
print(int(1.50))
print(complex(1.50))

print(10+5j)
print(int(10+5j))


