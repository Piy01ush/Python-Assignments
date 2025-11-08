# Author: Piyush Khare 
# Date: 08-Nov-2025
# Project Title: GradeBook Analyzer CLI 


import csv

print("Welcome to the GradeBook Analyzer!")
print()

while True:
    print("Menu:")
    print("1) Manual entry")
    print("2) Load from CSV file")
    print("3) Exit")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "3":
        print("Goodbye!")
        break

    students = []

    if choice == "1":
        try:
            n = int(input("How many students? "))
        except:
            print("Invalid number.")
            continue

        for i in range(n):
            name = input("Enter student name: ")
            try:
                marks = float(input("Enter marks for " + name + ": "))
            except:
                print("Invalid marks, set to 0.")
                marks = 0
            students.append([name, marks])

    elif choice == "2":
        file_name = input("Enter CSV file path: ").strip()
        try:
            with open(file_name, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) < 2:
                        continue
                    name = row[0].strip()
                    try:
                        marks = float(row[1].strip())
                    except:
                        continue
                    students.append([name, marks])
        except:
            print("File not found or unreadable.")
            continue
    else:
        print("Invalid choice.")
        continue

    if len(students) == 0:
        print("No data to analyze.")
        continue

    # Calculate average
    total = 0
    for s in students:
        total += s[1]
    average = total / len(students)

    # Calculate median
    scores = sorted([s[1] for s in students])
    mid = len(scores) // 2
    if len(scores) % 2 == 1:
        median = scores[mid]
    else:
        median = (scores[mid - 1] + scores[mid]) / 2

    # Find highest and lowest
    highest = students[0]
    lowest = students[0]
    for s in students:
        if s[1] > highest[1]:
            highest = s
        if s[1] < lowest[1]:
            lowest = s

    # Assign grades
    graded = []
    for s in students:
        score = s[1]
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        graded.append([s[0], s[1], grade])

    # Pass/fail lists
    passed = [s[0] for s in students if s[1] >= 40]
    failed = [s[0] for s in students if s[1] < 40]

    # Display summary
    print("\n------ Analysis Summary ------")
    print("Average:", round(average, 2))
    print("Median:", median)
    print("Highest:", highest[0], "-", highest[1])
    print("Lowest:", lowest[0], "-", lowest[1])
    print("Passed (>=40):", passed)
    print("Failed (<40):", failed)

    print("\nName\t\tMarks\tGrade")
    print("--------------------------------")
    for g in graded:
        print(g[0], "\t", g[1], "\t", g[2])
    print("--------------------------------")

    # Save option
    save = input("\nDo you want to save results to CSV? (yes/no): ").strip().lower()
    if save == "yes":
        out_file = input("Enter filename (example: results.csv): ").strip()
        try:
            with open(out_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Name", "Marks", "Grade"])
                for g in graded:
                    writer.writerow(g)
            print("Results saved to", out_file)
        except:
            print("Error saving file.")

    print("\nReturning to main menu...\n")
