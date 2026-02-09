# Q4 Loop + Condition Interaction

numbers = [3, 7, 2, 9, 4]
total = 0

for n in numbers:
    if n % 2 == 0:
        total += n

print(total)

# 'for' loop inputs n=3,7,2,9,4 in this order.
# When n=3, n is not even. So if exit and back to for loop again. ->not good, 3%2=1, so it is not 0.
# When n=7, n is not even. So if exit and back to for loop again.
# When n=2, n is even and n%2==0 is True. 'total' changes to 2
# Continuing those, total=2+4=6
# This program prints 6
