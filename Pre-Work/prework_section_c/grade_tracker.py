import csv


def load_students(filepath):
    students = []

    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append(row)

    except FileNotFoundError:
        print(f"Error: Could not find file '{filepath}'.")
        return []

    return students


def calculate_average(grades):
    valid_grades = []

    for grade in grades:
        if grade != "":
            valid_grades.append(float(grade))

    if len(valid_grades) == 0:
        return None

    average = sum(valid_grades) / len(valid_grades)

    return round(average, 1)


def get_letter_grade(average):
    if average is None:
        return "N/A"
    elif average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def generate_report(students):
    grade_distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0,
        "N/A": 0
    }

    student_results = []
    valid_averages = []

    for student in students:
        grades = [
            student["math"],
            student["science"],
            student["english"],
            student["history"]
        ]

        average = calculate_average(grades)
        letter_grade = get_letter_grade(average)

        student_result = {
            "student_name": student["student_name"],
            "average": average,
            "letter_grade": letter_grade
        }

        student_results.append(student_result)
        grade_distribution[letter_grade] += 1

        if average is not None:
            valid_averages.append(average)

    if len(valid_averages) > 0:
        class_average = round(
            sum(valid_averages) / len(valid_averages),
            1
        )

        highest_average = max(valid_averages)
        lowest_average = min(valid_averages)

    else:
        class_average = None
        highest_average = None
        lowest_average = None

    report = {
        "total_students": len(students),
        "class_average": class_average,
        "highest_average": highest_average,
        "lowest_average": lowest_average,
        "grade_distribution": grade_distribution,
        "student_results": student_results
    }

    return report


def write_report(report, filepath):
    with open(filepath, "w") as file:
        file.write("GRADE REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write("CLASS SUMMARY\n")
        file.write("-" * 40 + "\n")

        file.write(
            f"Total students: {report['total_students']}\n"
        )

        if report["class_average"] is not None:
            file.write(
                f"Class average: {report['class_average']:.1f}\n"
            )
            file.write(
                f"Highest average: {report['highest_average']:.1f}\n"
            )
            file.write(
                f"Lowest average: {report['lowest_average']:.1f}\n"
            )
        else:
            file.write("Class average: N/A\n")
            file.write("Highest average: N/A\n")
            file.write("Lowest average: N/A\n")

        file.write("\nGRADE DISTRIBUTION\n")
        file.write("-" * 40 + "\n")

        for grade, count in report["grade_distribution"].items():
            file.write(f"{grade}: {count}\n")

        file.write("\nINDIVIDUAL STUDENT RESULTS\n")
        file.write("-" * 40 + "\n")

        for student in report["student_results"]:
            name = student["student_name"]
            average = student["average"]
            letter_grade = student["letter_grade"]

            if average is None:
                file.write(
                    f"{name}: N/A ({letter_grade})\n"
                )
            else:
                file.write(
                    f"{name}: {average:.1f} ({letter_grade})\n"
                )


def main():
    print("Loading student data...")

    students = load_students("data/students.csv")

    print(f"  Loaded {len(students)} students.")

    if len(students) == 0:
        return

    print("\nGenerating report...")

    report = generate_report(students)

    print("\n--- Summary ---")
    print(f"Total students:   {report['total_students']}")
    print(f"Class average:    {report['class_average']}")
    print(f"Highest average:  {report['highest_average']}")
    print(f"Lowest average:   {report['lowest_average']}")

    print("\nGrade Distribution:")

    for grade, count in report["grade_distribution"].items():
        print(f"  {grade}: {count}")

    print("\nTop 5 students:")

    valid_students = [
        student
        for student in report["student_results"]
        if student["average"] is not None
    ]

    valid_students.sort(
        key=lambda student: student["average"],
        reverse=True
    )

    for student in valid_students[:5]:
        print(
            f"  {student['student_name']:<20} "
            f"{student['average']:.1f} "
            f"({student['letter_grade']})"
        )

    write_report(report, "grade_report.txt")

    print("\nReport written to grade_report.txt")


if __name__ == "__main__":
    main()