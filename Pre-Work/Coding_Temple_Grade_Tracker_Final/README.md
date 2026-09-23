# Student Grade Tracker

## Overview

This command line Python application reads student grade data from a CSV file, calculates individual and class statistics, handles missing values, and writes a formatted report to `grade_report.txt`.

## Project Structure

```text
grade_tracker_project/
├── data/
│   └── students.csv
├── grade_tracker.py
├── requirements.txt
├── grade_report.txt
└── README.md
```

## Requirements

Python 3 is required.

No external packages are needed. The project uses Python's built in `csv` module, so `requirements.txt` does not contain package dependencies.

## How to Run

Open a terminal in the project folder and run:

```bash
python3 grade_tracker.py
```

The program will:

1. Read `data/students.csv`
2. Display the number of students loaded
3. Calculate individual student averages and letter grades
4. Calculate class statistics and the grade distribution
5. Display the top five students
6. Write the complete report to `grade_report.txt`

## Error Handling

The program handles a missing CSV file by printing a helpful message and returning an empty list.

Missing grade values are skipped when calculating averages.

If a student has no valid grades, that student receives an average of `None` internally and a letter grade of `N/A`.

Non numeric grade values are also skipped so an unexpected value does not crash the program.

## Functions

`load_students(filepath)` reads the CSV file and returns student records as dictionaries.

`calculate_average(grades)` skips missing values and returns a rounded numeric average or `None`.

`get_letter_grade(average)` converts a numeric average into A, B, C, D, F, or N/A.

`generate_report(students)` builds the class summary, grade distribution, and individual results.

`write_report(report, filepath)` writes the complete formatted report to a text file.

## Verification

The program was tested with the provided 15 student CSV records.

Using the provided data, the calculated values are:

Total students: 15  
Class average: 79.4  
Highest average: 95.2  
Lowest average: 58.2  

Grade distribution:

A: 3  
B: 4  
C: 5  
D: 2  
F: 1  
N/A: 0

The provided assignment's sample terminal output lists a class average of 80.1 and a B/C distribution of 5/4. Those sample values do not match the CSV rows in the project brief. This project calculates directly from the supplied CSV data.
