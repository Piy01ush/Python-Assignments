# Author: Piyush Khare
# Date: 08-Nov-2025
# Project Title: Daily Calorie Tracker CLI

print("Welcome to the Daily Calorie Tracker!")
print("This program helps you keep track of your daily calorie intake.\n")

num_meals = int(input("How many meals do you want to enter? "))

meals = []
calories = []

for i in range(num_meals):
    meal = input("Enter meal name: ")
    cal = int(input("Enter calories for " + meal + ": "))
    meals.append(meal)
    calories.append(cal)

total = sum(calories)
average = total / len(calories)

limit = int(input("\nEnter your daily calorie limit: "))

if total > limit:
    status = "You have exceeded your calorie limit!"
else:
    status = "You are within your calorie limit."

print("\n---- Calorie Report ----")
print("Meal Name\tCalories")
print("------------------------")

for i in range(len(meals)):
    print(meals[i], "\t", calories[i])

print("------------------------")
print("Total:", total)
print("Average:", round(average, 2))
print(status)

save = input("\nDo you want to save this report to a file? (yes/no): ").lower()

if save == "yes":
    file = open("calorie_log.txt", "w")
    file.write("Calorie Tracker Report\n")
    file.write("------------------------\n")
    file.write("Meal Name\tCalories\n")
    for i in range(len(meals)):
        file.write(meals[i] + "\t" + str(calories[i]) + "\n")
    file.write("------------------------\n")
    file.write("Total: " + str(total) + "\n")
    file.write("Average: " + str(round(average, 2)) + "\n")
    file.write("Daily Limit: " + str(limit) + "\n")
    file.write(status + "\n")
    file.close()
    print("Report saved to calorie_log.txt")
else:
    print("Report not saved.")

print("\nThanks for using the program!")
