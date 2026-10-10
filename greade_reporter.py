# Grade Reporter Program

# Given list of scores (Do not change these numbers)
scores = [72, 45, 90, 61, 38]

passed_count = 0
failed_count = 0
total_score = 0

# Use a for loop to go through every score in the list
for score in scores:
    # Use if / elif / else to determine the grade based on criteria
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    # Print each score with its grade on its own line
    print(f"Score: {score} - Grade: {grade}")
    
    # Count passes and fails (score of 50 or more is a pass)
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1
        
    # Accumulate the total score
    total_score += score

# Calculate the average and round to one decimal place
average_score = round(total_score / len(scores), 1)

print("-" * 30)
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Average: {average_score}")
