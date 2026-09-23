import csv


def load_students(filepath):
    """Read student records from a CSV file and return a list of dictionaries."""
    try:
        with open(filepath, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: Could not find file '{filepath}'.")
        return []


def calculate_average(grades):
    """Return the average of valid grade values rounded to one decimal place."""
    valid_grades = []

    for grade in grades:
        if grade is None:
            continue

        grade_text = str(grade).strip()
        if grade_text == "":
            continue

        try:
            valid_grades.append(float(grade_text))
        except ValueError:
            continue

    if not valid_grades:
        return None

    return round(sum(valid_grades) / len(valid_grades), 1)


def get_letter_grade(average):
    """Convert a numeric average into a letter grade."""
    if average is None:
        return "N/A"
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def generate_report(students):
    """Build class statistics, grade distribution, and individual results."""
    distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0,
        "F": 0,
        "N/A": 0,
    }

    individual_results = []
    valid_averages = []

    for student in students:
        name = student.get("student_name", "Unknown Student")

        grades = [
            value
            for key, value in student.items()
            if key != "student_name"
        ]

        average = calculate_average(grades)
        letter_grade = get_letter_grade(average)

        individual_results.append(
            {
                "student_name": name,
                "average": average,
                "letter_grade": letter_grade,
            }
        )

        distribution[letter_grade] += 1

        if average is not None:
            valid_averages.append(average)

    if valid_averages:
        class_average = round(sum(valid_averages) / len(valid_averages), 1)
        highest_average = max(valid_averages)
        lowest_average = min(valid_averages)
    else:
        class_average = None
        highest_average = None
        lowest_average = None

    return {
        "total_students": len(students),
        "class_average": class_average,
        "highest_average": highest_average,
        "lowest_average": lowest_average,
        "grade_distribution": distribution,
        "individual_results": individual_results,
    }


def write_report(report, filepath):
    """Write the full formatted class report to a text file."""
    with open(filepath, "w", encoding="utf-8") as file:
        file.write("STUDENT GRADE REPORT\n")
        file.write("=" * 50 + "\n\n")

        file.write("CLASS SUMMARY\n")
        file.write("-" * 50 + "\n")
        file.write(f"Total students:   {report['total_students']}\n")
        file.write(
            f"Class average:    {format_average(report['class_average'])}\n"
        )
        file.write(
            f"Highest average:  {format_average(report['highest_average'])}\n"
        )
        file.write(
            f"Lowest average:   {format_average(report['lowest_average'])}\n\n"
        )

        file.write("GRADE DISTRIBUTION\n")
        file.write("-" * 50 + "\n")
        for grade in ["A", "B", "C", "D", "F", "N/A"]:
            file.write(
                f"{grade:<3} {report['grade_distribution'][grade]}\n"
            )

        file.write("\nINDIVIDUAL STUDENT RESULTS\n")
        file.write("-" * 50 + "\n")
        file.write(f"{'Student':<24}{'Average':>10}{'Grade':>10}\n")
        file.write("-" * 50 + "\n")

        for student in report["individual_results"]:
            average = format_average(student["average"])
            file.write(
                f"{student['student_name']:<24}"
                f"{average:>10}"
                f"{student['letter_grade']:>10}\n"
            )


def format_average(average):
    """Format an average for display without changing report calculations."""
    if average is None:
        return "N/A"
    return f"{average:.1f}"


def main():
    print("Loading student data...")
    students = load_students("data/students.csv")

    if not students:
        print("No student data available. Program ending.")
        return

    print(f"  Loaded {len(students)} students.")

    print("\nGenerating report...")
    report = generate_report(students)

    print("\n--- Summary ---")
    print(f"Total students:   {report['total_students']}")
    print(f"Class average:    {format_average(report['class_average'])}")
    print(f"Highest average:  {format_average(report['highest_average'])}")
    print(f"Lowest average:   {format_average(report['lowest_average'])}")

    print("\nGrade Distribution:")
    for grade in ["A", "B", "C", "D", "F", "N/A"]:
        print(f"  {grade}: {report['grade_distribution'][grade]}")

    valid_students = [
        student
        for student in report["individual_results"]
        if student["average"] is not None
    ]
    top_students = sorted(
        valid_students,
        key=lambda student: student["average"],
        reverse=True,
    )[:5]

    print("\nTop 5 students:")
    for student in top_students:
        print(
            f"  {student['student_name']:<20}"
            f"{student['average']:>5.1f}  "
            f"({student['letter_grade']})"
        )

    output_file = "grade_report.txt"
    write_report(report, output_file)
    print(f"\nReport written to {output_file}")


if __name__ == "__main__":
    main()
