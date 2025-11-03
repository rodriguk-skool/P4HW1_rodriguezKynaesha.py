# Kynaesha Rodriguez
# 11/2/25
# P4HW1
# This program asks the user for test scores, drops the lowest one,
# and then shows the average and letter grade.

# pseudocode
# ask for number of scores
# loop to collect scores, validate they are between 0 and 100
# store scores in a list
# drop the lowest score
# calculate average and display letter grade

scores = []  

num_scores = int(input("How many scores do you want to enter? "))

for i in range(num_scores):
    score = float(input(f"Enter score #{i+1}: "))

    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i+1} again: "))

    scores.append(score)

lowest = min(scores)
scores.remove(lowest)

average = sum(scores) / len(scores)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("\n------------Results------------")
print("Lowest Score  :", format(lowest, ".1f"))
print("Modified List :", scores)
print("Scores Average:", format(average, ".2f"))
print("Grade         :", grade)
print("--------------------------------")