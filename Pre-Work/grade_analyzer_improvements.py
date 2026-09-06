def calculate_stats(numbers):
    """Calculate statistics for a list of numeric scores."""

    if len(numbers) == 0:
        return None

    valid_numbers = []

    for number in numbers:
        try:
            valid_numbers.append(float(number))
        except (ValueError, TypeError):
            print(f"Skipping invalid score: {number}")

    if len(valid_numbers) == 0:
        return None

    total = sum(valid_numbers)
    average = total / len(valid_numbers)

    above_average = []

    for number in valid_numbers:
        if number > average:
            above_average.append(number)

    return {
        "total": total,
        "average": average,
        "highest": max(valid_numbers),
        "lowest": min(valid_numbers),
        "above_average": above_average,
        "above_count": len(above_average)
    }


scores = [85, 92, 78, 95, 88, 70, 93]

result = calculate_stats(scores)

if result is None:
    print("No valid scores available.")
else:
    print(f"Total: {result['total']}")
    print(f"Average: {result['average']:.2f}")
    print(f"Highest: {result['highest']}")
    print(f"Lowest: {result['lowest']}")
    print(f"Above average: {result['above_count']} scores")