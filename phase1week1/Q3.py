# Q3 List processing
# numbers = [3,7,2,9,4]
# Write code that:
# Calculates the sum of even numbers only
# Prints the result

numbers = [3, 7, 2, 9, 4]
ans = 0

for num in numbers:
    if num % 2 == 0:
        ans += num

print(f"The answer is {ans}")