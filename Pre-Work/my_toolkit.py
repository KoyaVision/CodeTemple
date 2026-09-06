def calculate_average(numbers):
    """Returns the average of a list of numbers. Returns 0 if the list is empty."""

    if len(numbers) == 0:
        return 0

    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


def find_max_and_min(numbers):
    """Returns the largest and smallest values in a list as a tuple."""

    if len(numbers) == 0:
        return (None, None)

    max_value = numbers[0]
    min_value = numbers[0]

    for number in numbers:
        if number > max_value:
            max_value = number

        if number < min_value:
            min_value = number

    return (max_value, min_value)


def count_occurrences(items, target):
    """Returns how many times a target value appears in a list."""

    count = 0

    for item in items:
        if item == target:
            count += 1

    return count


def is_palindrome(text):
    """Returns True if text reads the same forward and backward, ignoring spaces and case."""

    cleaned_text = text.replace(" ", "").lower()

    return cleaned_text == cleaned_text[::-1]


def create_report(title, scores):
    """Creates and returns a formatted report using a list of scores."""

    average = calculate_average(scores)
    max_value, min_value = find_max_and_min(scores)

    report = (
        f"{title}\n"
        f"Average: {average:.2f}\n"
        f"Maximum: {max_value}\n"
        f"Minimum: {min_value}"
    )

    return report


if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]

    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))

    # Edge case tests
    print()
    print("EDGE CASE TESTS")

    # Empty lists
    print(f"Empty average: {calculate_average([])}")
    print(f"Empty max/min: {find_max_and_min([])}")

    # Multiple occurrences
    print(f"Count multiple 85s: {count_occurrences([85, 90, 85, 70, 85], 85)}")

    # Palindrome edge cases
    print(f"Phrase with spaces: {is_palindrome('A man a plan a canal Panama')}")
    print(f"Single character: {is_palindrome('A')}")
    print(f"Mixed case: {is_palindrome('RaceCar')}")