# Q5 'break' vs 'continue'

for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)

# 'i' will be i=0,1,2,3,4
# When i=4, this goes to break and exits 'for' loop including print(i)
# This program prints 0,1,2,3
