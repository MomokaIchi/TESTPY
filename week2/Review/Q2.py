# Equality vs Truthiness
# What is printed? And explain both lines separately.

x = []

if x == False:
    print("Equal")
if not x:
    print("Not")

# Not
# Because [] itself is not False even if bool([]) is False.
# So x==False This is False.
# When if is written if (not) x:, this "if" checks bool(x) is T or F.
# bool([]) is F, so not x is T.