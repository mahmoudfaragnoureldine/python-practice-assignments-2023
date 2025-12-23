# -----------------------
# -- Built In Function --
# -----------------------
# sum()
# round()
# range()
# print()
# -----------------------

# sum(itrerable, start)

a = [1, 10, 19, 40]
print(sum(a))       # 70
print(sum(a, 40))   # 110

# round(number, numfdigits) # بتقرب الرقم العشرى

print(round(150.6))
print(round(150.555, 2))

# range(start, end, step)

print(list(range(0)))
print(list(range(10)))
print(list(range(0, 20, 2)))

# print()
print("Hello Walid")  # print 1 massege
print("Hello", "Walid" , sep="#") # print 2 masseges

print('first line', end=" ")
print('second line', end='\n') 