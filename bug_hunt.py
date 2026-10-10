count = 1
total = 0

# BUG: Added missing colon (:) at the end of the while loop statement.
# BUG: Changed '< 5' to '<= 5' so the loop includes 5, fixing the logical boundary bug that caused the sum to be 10 instead of 15.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Converted the integer variable `total` to a string using str(total) to fix the TypeError when concatenating with a string.
print("Sum of 1 to 5 is: " + str(total))
