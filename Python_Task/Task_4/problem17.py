# 17. Finding the Percentage

if __name__ == '__main__':
    n = int(input("Enter the no. of students: "))
    student_marks = {}
    for _ in range(n):
        name, *line = input("Enter the student name and marks : ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter the name of the student to query: ")
    
 # FIX 1 & 2: Changed () to [] and matched the spelling of query_score
    query_score = student_marks[query_name]
    
    # FIX 3: Kept variable name lowercase to match the print statement
    avg_score = sum(query_score) / len(query_score)
    
    # BONUS FIX: Use an f-string to force exactly 2 decimal places (e.g., 56.00)
    print(f"{avg_score:.2f}")
