# Author: Piyush Khare
# Date: 2025-11-08
# A basic Python program to take student marks and analyze grades

print("Welcome to the GradeBook Analyzer!")
print("This program checks student marks and shows grades and results.\n")

def average(marks):
    total = 0
    for m in marks.values():
        total += m
    return total / len(marks)

def median(marks):
    data = sorted(marks.values())
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    else:
        return data[mid]

def max_score(marks):
    high_name = list(marks.keys())[0]
    high_value = marks[high_name]
    for name, value in marks.items():
        if value > high_value:
            high_name = name
            high_value = value
    return high_name, high_value

def min_score(marks):
    low_name = list(marks.keys())[0]
    low_value = marks[low_name]
    for name, value in marks.items():
        if value < low_value:
            low_name = name
            low_value = value
    return low_name, low_value

def give_grades(marks):
    grades = {}
    for name, mark in marks.items():
        if mark >= 90:
            grades[name] = "A"
        elif mark >= 80:
            grades[name] = "B"
        elif mark >= 70:
            grades[name] = "C"
        elif mark >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

def grade_count(grades):
    d = {"A":0,"B":0,"C":0,"D":0,"F":0}
    for g in grades.values():
        if g in d:
            d[g] += 1
    return d

def pass_fail(marks):
    passed = [n for n, m in marks.items() if m >= 40]
    failed = [n for n, m in marks.items() if m < 40]
    return passed, failed

def print_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("------------------------------")
    for n in marks:
        print(n, "\t", marks[n], "\t", grades[n])
    print("------------------------------")

while True:
    print("\nMenu:")
    print("1. Enter student data")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "2":
        print("Exiting program.")
        break

    marks = {}
    n = int(input("How many students? "))
    for i in range(n):
        name = input("Enter name: ")
        mark = float(input("Enter marks for " + name + ": "))
        marks[name] = mark

    avg = average(marks)
    med = median(marks)
    max_name, max_val = max_score(marks)
    min_name, min_val = min_score(marks)
    grades = give_grades(marks)
    count = grade_count(grades)
    passed, failed = pass_fail(marks)

    print("\n--- Grade Analysis ---")
    print("Average:", round(avg,2))
    print("Median:", med)
    print("Highest:", max_name, "-", max_val)
    print("Lowest:", min_name, "-", min_val)
    print("Grade Distribution:", count)
    print("Passed:", passed)
    print("Failed:", failed)

    print_table(marks, grades)
    print("\nDone!\n")
