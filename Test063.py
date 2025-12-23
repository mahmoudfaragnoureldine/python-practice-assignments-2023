#
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You need first to understand recursion --
# ---------------------------------------------------------------------

# هى فنكشن بتنادى نفسها جوه نفسها وبتنادى نفسها جوه نفسها وهكذا

# Test [ WWWoooorrrldd ]


def cleanWord(word):
    if len(word) == 1:
        return word

    if word[0] == word[1]:
        return cleanWord(word[1:])

    return word[0] + cleanWord(word[1:])


print(cleanWord("WWWoooorrrldd"))
