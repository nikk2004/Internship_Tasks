# 13. Nested Lists
# Hackerank Link : https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []

    n = int(input("Enter number of students: "))

    for _ in range(n):
        name = input("Enter student name: ")
        score = float(input("Enter student score: "))
        students.append([name, score])

    unique_score = sorted(set([student[1] for student in students]))

    second_lowest = unique_score[1]

    print("Students with the second lowest score:")

    for student in sorted(students):
        if student[1] == second_lowest:
            print(student[0])


''' Output :
Enter student score: 37.21
Enter student name: Tina
Enter student score: 37.2
Enter student name: Akriti
Enter student score: 41
Enter student name: Harsh
Enter student score: 39
Students with the second lowest score:
Berry
Harray
'''