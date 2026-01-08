# You see this code:
def process(age):
    if age >= 18:
        return True
    else:
        return False
# Rewrite it in a cleaner way
# Explain why it is better (1-2 sentences, simple English)

def process_rewrite(age) -> bool:
    return age >= 18
# I think by using "-> bool" I can redule return True or False
# but I could not get the way.