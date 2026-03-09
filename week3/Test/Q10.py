# Design question
# If you were building a backend for your idle game
# how might you model:
# Normal user/ Premium user/ Admin user

# Would inheritance make sence?
# Would composition (having objects inseide objects) make more sense?
# Explain your reasoning as a working design theory - not absolute truth

# I'm going to make Normal user and Premium user inheritance class so they can change class
# How ever, I'm going to make Admin user as a dependent class so Normal or Premium user can't chage
# class to Admin
