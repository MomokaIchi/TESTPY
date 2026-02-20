# Range Mechanics
# What is printed? And list values of i.

count = 0

for i in range(2, 8, 2):
    count += i

print(count)

# 10 or 12...
# I think it shows 10 because when i=2 in second time, this for loop notice this is the last.
# So quit this for loop before add to count

# 0+2+4+6 then stop