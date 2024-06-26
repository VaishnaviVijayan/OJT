def calculate_letter_grades(scores_dict):
    def get_letter_grade(average_score):
        if 90 <= average_score <= 100:
            return 'A'
        elif 80 <= average_score < 90:
            return 'B'
        elif 70 <= average_score < 80:
            return 'C'
        elif 60 <= average_score < 70:
            return 'D'
        else:
            return 'F'

    letter_grades_dict = {}
    for student, scores in scores_dict.items():
        average_score = sum(scores) / len(scores)
        letter_grades_dict[student] = get_letter_grade(average_score)

    return letter_grades_dict

# Example usage
student_scores = {
    "Alice": [85, 92, 88],
    "Bob": [78, 74, 80],
    "Charlie": [90, 91, 89],
    "Diana": [65, 70, 68],
    "Eve": [50, 55, 60]
}

letter_grades = calculate_letter_grades(student_scores)
print(letter_grades)
