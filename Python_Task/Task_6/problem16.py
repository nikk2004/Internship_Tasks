# 16.Check Subset
# Hackerrank Link : https://www.hackerrank.com/challenges/py-check-subset/problem
# Read the total number of test cases
t = int(input("Enter the number of test cases: "))

# Loop through each test case
for _ in range(t):
    # Read set A details
    num_elements_A = int(input("Enter the number of elements in set A: "))
    set_A = set(map(int, input("Enter the elements of set A: ").split()))
    
    # Read set B details
    num_elements_B = int(input("Enter the number of elements in set B: "))
    set_B = set(map(int, input("Enter the elements of set B: ").split()))
    
    # Check if set A is a subset of set B and print the result
    print(set_A.issubset(set_B))

'''output:
Enter the number of elements in set A: 1
Enter the elements of set A: 2
Enter the number of elements in set B: 5
Enter the elements of set B: 3 6 5 4 1
False
Enter the number of elements in set A: 7
Enter the elements of set A: 1 2 3 5 6 8 9
Enter the number of elements in set B: 3
Enter the elements of set B: 9 8 2
False
'''