"""
GPA Calculator
COS 102 Project

This program lets a student:
1. Add courses (course title, unit load, grade)
2. View all courses added so far
3. Calculate the semester GPA
4. Save course records to a file (gpa_records.csv)
5. Load previously saved records when the program starts

Grading scale used (5-point scale, common in Nigerian universities):
    A = 5 points
    B = 4 points
    C = 3 points
    D = 2 points
    E = 1 point
    F = 0 points
"""

import csv
import os

# Name of the file used to store course records
FILE_NAME = "gpa_records.csv"

# Mapping of letter grades to grade points
GRADE_POINTS = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 0
}


def load_courses():
    """
    Load course records from the CSV file (if it exists).
    Returns a list of dictionaries, e.g.:
    [{"course": "MTH 101", "unit": 3, "grade": "A"}, ...]
    """
    courses = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert unit back to integer since CSV stores everything as text
                row["unit"] = int(row["unit"])
                courses.append(row)

    return courses


def save_courses(courses):
    """
    Save the list of course dictionaries to the CSV file.
    """
    with open(FILE_NAME, mode="w", newline="") as file:
        fieldnames = ["course", "unit", "grade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for course in courses:
            writer.writerow(course)


def add_course(courses):
    """
    Ask the user for course details and add it to the courses list.
    """
    print("\n--- Add New Course ---")
    course_name = input("Enter course title (e.g. COS 102): ").strip().upper()

    # Validate unit input
    while True:
        unit_input = input("Enter course unit (e.g. 2, 3): ").strip()
        if unit_input.isdigit() and int(unit_input) > 0:
            unit = int(unit_input)
            break
        else:
            print("Invalid unit. Please enter a positive whole number.")

    # Validate grade input
    while True:
        grade = input("Enter grade obtained (A, B, C, D, E, F): ").strip().upper()
        if grade in GRADE_POINTS:
            break
        else:
            print("Invalid grade. Please enter one of: A, B, C, D, E, F")

    courses.append({"course": course_name, "unit": unit, "grade": grade})
    print(f"'{course_name}' added successfully!\n")


def view_courses(courses):
    """
    Display all courses currently entered.
    """
    print("\n--- Your Courses ---")

    if not courses:
        print("No courses added yet.\n")
        return

    print(f"{'Course':<12}{'Unit':<8}{'Grade':<8}{'Grade Point'}")
    print("-" * 40)

    for c in courses:
        grade_point = GRADE_POINTS[c["grade"]]
        print(f"{c['course']:<12}{c['unit']:<8}{c['grade']:<8}{grade_point}")

    print()


def calculate_gpa(courses):
    """
    Calculate and display the GPA based on entered courses.

    Formula:
        GPA = (sum of (unit * grade_point) for all courses) / (sum of units)
    """
    print("\n--- GPA Result ---")

    if not courses:
        print("You haven't added any courses yet. Add courses first.\n")
        return

    total_units = 0
    total_points = 0

    for c in courses:
        grade_point = GRADE_POINTS[c["grade"]]
        total_units += c["unit"]
        total_points += grade_point * c["unit"]

    gpa = total_points / total_units

    print(f"Total Units: {total_units}")
    print(f"Total Grade Points: {total_points}")
    print(f"Your GPA is: {gpa:.2f}\n")


def show_menu():
    """
    Display the main menu options.
    """
    print("=" * 40)
    print("        GPA CALCULATOR - COS 102")
    print("=" * 40)
    print("1. Add Course")
    print("2. View Courses")
    print("3. Calculate GPA")
    print("4. Save and Exit")
    print("=" * 40)


def main():
    """
    Main program loop.
    """
    courses = load_courses()

    if courses:
        print(f"Loaded {len(courses)} saved course(s) from previous session.\n")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_course(courses)
        elif choice == "2":
            view_courses(courses)
        elif choice == "3":
            calculate_gpa(courses)
        elif choice == "4":
            save_courses(courses)
            print("\nRecords saved to 'gpa_records.csv'. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a number from 1 to 4.\n")


if __name__ == "__main__":
    main()
