# ------------------------
# -- Break, Continue, Pass
# ------------------------

myNumber = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# Continue

for number in myNumber:
    if number == 13:
        continue  # skip 13 and countinue

    print(number)

print("#" * 40)

# Break

for number in myNumber:
    if number == 13:
        break  # break the loop

    print(number)

print("#" * 40)

# Pass

for number in myNumber:
    if number == 13:
        pass  # عدى الموضوع

    print()

print("#" * 40)
