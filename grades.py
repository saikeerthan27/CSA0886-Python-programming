def validate_marks(marks):
    """Validate the input marks."""
    if not isinstance(marks, (int, float)):
        raise ValueError("Marks must be a number.")
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")
    return True

def calculate_grade(marks):
    """Calculate the grade based on the marks."""
    if 90 <= marks <= 100:
        return 'A'
    elif 80 <= marks < 90:
        return 'B'
    elif 70 <= marks < 80:
        return 'C'
    elif 60 <= marks < 70:
        return 'D'
    else:
        return 'F'

def main():
    try:
        marks = float(input("Enter the student's marks (0-100): "))
        if validate_marks(marks):
            grade = calculate_grade(marks)
            print(f"The grade for the marks {marks} is: {grade}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
