# True or False(explain in sentence):
# if is_active == True:
# Is this good style?

# It works, but this is cleaner:
def active_check(is_active) -> bool:
    return is_active