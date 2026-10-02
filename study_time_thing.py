import json
from pathlib import Path

DATA_FILE = Path("study_data.json")


def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_assignment(data):
    course = input("Enter the course name: ").strip()

    if course == "":
        print("Enter a name.")
        return

    assignment = input("Enter the assignment name: ").strip()

    try:
        grade = float(input("Enter the grade percentage: "))
        hours = float(input("Enter hours spent on this assignment: "))
    except ValueError:
        print("Please enter numbers for the grade and hours.")
        return

    if grade < 0 or grade > 100 or hours < 0:
        print("Please enter a grade from 0-100 and a positive number of hours.")
        return

    if course not in data:
        data[course] = []

    data[course].append({
        "name": assignment,
        "grade": grade,
        "hours": hours
    })

    save_data(data)
    print("Assignment added successfully.")


def show_course_analysis(data):
    if not data:
        print("There is no data yet.")
        return

    print("\nCourse Analysis")

    for course, assignments in data.items():
        total_grade = 0
        total_hours = 0

        for assignment in assignments:
            total_grade += assignment["grade"]
            total_hours += assignment["hours"]

        average_grade = total_grade / len(assignments)

        print("\n" + course)
        print(f"Average grade: {average_grade:.1f}%")
        print(f"Total study/work time: {total_hours:.1f} hours")

        if total_hours > 0:
            grade_per_hour = average_grade / total_hours
            print(f"Grade percentage per hour: {grade_per_hour:.1f}")

        if average_grade >= 90:
            print(" Your grades are strong. You may not need to spend much more time on this class.")
        elif average_grade >= 75:
            print( "Your grades are okay. More study time may help improve them.")
        else:
            print(" Your grades are low. Consider spending more time studying or getting help.")


def show_assignments(data):
    if not data:
        print("There is no data yet.")
        return

    for course, assignments in data.items():
        print("\n" + course)

        for assignment in assignments:
            print(
                f"{assignment['name']} - "
                f"{assignment['grade']:.1f}% - "
                f"{assignment['hours']:.1f} hours"
            )



def main():
    data = load_data()

    while True:
        print("\n===== Study Time Analyzer =====")
        print("1. Add assignment")
        print("2. View assignments")
        print("3. View course analysis")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()
        print(f"You selected: {choice}")

        if choice == "1":
            add_assignment(data)
        elif choice == "2":
            show_assignments(data)
        elif choice == "3":
            show_course_analysis(data)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

