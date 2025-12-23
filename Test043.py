# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

Country = "KS"

if Country == "Egypt":
    print(f"The weather in {Country} is 15")

elif Country == "KSA":
    print(f"The Weatheer in {Country} is 30")

else:
    print("Your country is not in the list")


# Short If

movieRate = 18
age = 16

if age < movieRate:
    print("Movie is not good for  you")  # Condition If True

else:
    print("Movie is good for you")  # Condition If False


print(
    "Movie is not good for you"
    if age < movieRate
    else "Movie is good for you and happy watch"
)

# Condition if Trur | If Condition | Else | Condition If False
