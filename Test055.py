# ------------------------
# -- Advaned Dictionary --
# ------------------------

mySkills = {"Html": "80%", "Css": "90%", "Js": "70%", "PHP": "80%"}

# print(mySkills.items())

# for skill in mySkills:
#    print(f"{skill} => {mySkills[skill]}")

# for key, value in mySkills.items():
#    print(f"{key} => {value}")

myUltimateSkills = {
    "Html": {"Main": "80%", "Pugs": "80%"},
    "Css": {"Main": "90%", "Sass": "70%"},
}

for main_key, main_value in myUltimateSkills.items():
    print(main_key)

    for child_key, child_value in main_value.items():
        print(f"{child_key} => {child_value}")
