
import csv

# Creating a fictional student dataset
students = [
    ["CU001", "Computer Science", 300, 90, 85],
    ["CU002", "Mass Communication", 200, 75, 68],
    ["CU003", "Accounting", 300, 95, 92],
    ["CU004", "Computer Science", 200, 80, 74],
    ["CU005", "Cyber Security", 300, 88, 81],
    ["CU006", "Business Administration", 100, 70, 65],
    ["CU007", "Computer Science", 300, 85, 78],
    ["CU008", "Accounting", 200, 92, 88],
    ["CU009", "Cyber Security", 100, 78, 72],
    ["CU010", "Mass Communication", 300, 96, 90]
]

# Dataset column headings
headers = [
    "Student ID",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score"
]

# Create and save the CSV file
with open("student_dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(students)

print("Student dataset created successfully!")
