# ---------------------------
# -- Practical Slice Emial --
# ---------------------------

theName = input('What\'s your name?').strip().capitalize()
theEmail = input('What\'s your email?').strip()

theUserName = theEmail[: theEmail.index('@')]
theWebsit = theEmail[theEmail.index('@') + 1 :]

print(f'your name is {theName}, your user name is {theUserName} and your websit is {theWebsit}.')

#email = "waleedfarag8@gmail.com"
#print(email[: email.index('@')])  # waleedfarag8


