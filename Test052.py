# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------

# Range

# myRange = range(1, 101)

# for number in myRange:
#   print(number)

mySkills = {"Html": "90%", "Css": "60%", "PHP": "70%", "Js": "80%", "Python": "90%"}

# print(mySkills["Js"])
# print(mySkills.get("Python"))

for skill in mySkills:
    # print(skill)

    print(f"My progress in Lang {skill} is: {mySkills[skill]}")
