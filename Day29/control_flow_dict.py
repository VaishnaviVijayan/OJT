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

# Example usage:
scores = {
    'Alice': [85, 90, 92],
    'Bob': [70, 75, 80],
    'Charlie': [60, 62, 58],
    'David': [95, 98, 100]
}

letter_grades = calculate_letter_grades(scores)
print(letter_grades)
