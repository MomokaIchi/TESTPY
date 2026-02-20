# Empty vs Zero
# What is printed?

values = ["", 0, None, "hi"]

for v in values:
    if v:
        print("T")
    else:
        print("F")