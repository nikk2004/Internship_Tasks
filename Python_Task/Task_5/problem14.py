# 14.Finding the percentage
# Hackerrank Link :https://www.hackerrank.com/challenges/finding-the-percentage/problem
 
if __name__ == '__main__':
    n = int(input("Enter number of students: "))
    student_marks = {}

    for _ in range(n):
        name, *line = input("Enter name and marks: ").split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input("Enter student name to find average: ")

    query_score = student_marks[query_name]

    avg_score = sum(query_score) / len(query_score)

    print(f"Average marks: {avg_score:.2f}")


''' Output :
Enter number of students: 3
Enter name and marks: Krishna 67 68 69
Enter name and marks: Arjun 70 98 63
Enter name and marks: Malika 52 56 60
Enter student name to find average: Malika
Average marks: 56.00
'''