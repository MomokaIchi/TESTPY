# Empty vs Zero
# What is printed?

values = ["", 0, None, "hi"]

for v in values:
    if v:
        print("T")
    else:
        print("F")

# if v: means if bool(v):
# bool("")=False, bool(0)=False, bool(None)=False, bool("hi")=True
# FFFT