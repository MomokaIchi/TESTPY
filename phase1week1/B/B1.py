# Rewrite without else:

# def can_vote(age):
#     if age < 18:
#         return False
#     else:
#         return True
    
def can_vote_clean(age) -> bool:
    return age >= 18
