# Slightly Evil Logic Test

x = "" # original x = 0
if x == False:
    print("Equal")
if not x:
    print("Not")

# 1. What lines are printed?
# 2. Why is this not a contradiction?

# Equal
# Not
# I thought 0, None, (and maybe one or two more?) are False
# In addtion, "if x:"" means "if x==True", therefore this if is the same meaning as first one\

# reasoning is not good
# Check 0=False, this is True so print works.
# But next one Checks x itself shows True or not

# False list: 0, 0.0, "", [], {}, None, False

