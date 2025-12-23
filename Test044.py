# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------

# A very beautifull note
print("#" * 80)
print(
    " You can write the first letter or the full name of the time unit ".center(80, "#")
)
print("#" * 80)

# Collect age date
age = input("Please write your age: ").strip()

# Collect time unit date
unit = input("Please choice time unite: Months, Weeks, Days? ").strip().lower()

# Get time units
months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if unit == "months" or unit == "m":
    print("You choice the unit Months")
    print(f"You lived for {months:,} Months.")

elif unit == "weeks" or unit == "w":
    print("You choice the unit Weeks")
    print(f"You lived for {weeks:,} Weeks.")

else:
    print("You choice the unit days")
    print(f"You lived for {days:,} Days.")
