# 13. Set .union() Operation

# Hackerank Link : https://www.hackerrank.com/challenges/py-set-union/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of English newspaper subscribers (not strictly needed for calculation)
n = int(input("Enter the number of English newspaper subscribers: "))
# Read the English subscribers' roll numbers into a set
english_subs = set(map(int, input("Enter the roll numbers of English subscribers: ").split()))

# Read the number of French newspaper subscribers (not strictly needed for calculation)
m = int(input("Enter the number of French newspaper subscribers: "))
# Read the French subscribers' roll numbers into a set
french_subs = set(map(int, input("Enter the roll numbers of French subscribers: ").split()))

# Use the union operator (|) or .union() to combine both sets and find the total unique count
total_unique_subs = english_subs.union(french_subs)

# Print the number of students with at least one subscription
print(len(total_unique_subs))


'''output : 
Enter the number of English newspaper subscribers: 9
Enter the roll numbers of English subscribers: 1 2 3 4 5 6 7 8 9
Enter the number of French newspaper subscribers: 9
Enter the roll numbers of French subscribers: 10 1 2 3 11 21 55 6 8
13
'''