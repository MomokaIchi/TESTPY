# Q2. if/elif/else Flow

score = 75
if score >= 90:
    result = "A"
elif score >= 80:
    result = "B"
elif score >= 70:
    result = "C"
elif score >= 60:
    result = "D"
else:
    result = "F"

print(result)

# C
# This program checks "A", "B", "C" parts but it doesn't check else: part 
# because "C" part is True ->X
# This if exits when True are shown