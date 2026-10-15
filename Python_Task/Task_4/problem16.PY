# 16. Nested Lists

if __name__ == '__main__':
    students = []
    for _ in range(int(input("Enter the no. of students: "))):
        name = input("Enter the student name: ")
        score = float(input("Enter the student score: "))
        students.append([name, score])

    # Find the second lowest grade
    grades = sorted(set([score for name, score in students]))
    second_lowest_grade = grades[1]

    # Find all students with the second lowest grade
    second_lowest_students = [name for name, score in students if score == second_lowest_grade]

    # Print the names of students with the second lowest grade
    for name in sorted(second_lowest_students):
        print(name)