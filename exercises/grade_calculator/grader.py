def letter_grade(score):
    """
    Convert a numeric score to a letter grade.

    Args:
        score (float): The numeric score (0-100).

    Returns:
        str: The corresponding letter grade.
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def convert_grades(student_grades):
    """
    Convert a list of student grades from numeric to letter grades.

    Args:
        student_grades (Dict[student_name, letter_grade]): A dictionary where the keys are student names and the values are their letter grades.

    Returns:
        Dict of {student_name: letter_grade} pairs.
    """
    return {student: letter_grade for student, letter_grade in student_grades.items()}

def group(student_letter_grades):
    """
    Group students by their letter grades.

    Args:
        student_letter_grades (Dict[student_name, letter_grade]): A dictionary where the keys are student names and the values are their letter grades.

    Returns:
        Dict of {letter_grade: [student_names]} pairs.
    """
    grouped = {}
    for student, grade in student_letter_grades.items():
        if grade not in grouped:
            grouped[grade] = []
        grouped[grade].append(student)
    return grouped

students = {
    "Alice": 95,
    "Bob": 82,
    "Charlie": 67,
    "David": 74,
    "Eve": 88,
    "Frank": 59,
    "Grace": 91,
    "Heidi": 76,
    "Ivan": 84,
    "Judy": 69,
    "Mallory": 92,
}

grades = convert_grades({student: letter_grade(score) for student, score in students.items()})
grouped_students = group(grades)