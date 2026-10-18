# 15. Set .difference() Operation
# Hackerrank Link : https://www.hackerrank.com/challenges/py-set-difference-operation/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read the number of English newspaper subscribers
n = int(input("Enter the number of English newspaper subscribers: "))
# Read the English subscribers' roll numbers into a set
english_subs = set(map(int, input("Enter the roll numbers of English subscribers: ").split()))

# Read the number of French newspaper subscribers
m = int(input("Enter the number of French newspaper subscribers: "))
# Read the French subscribers' roll numbers into a set
french_subs = set(map(int, input("Enter the roll numbers of French subscribers: ").split()))

# Use the difference operator (-) or .difference() to find elements only in English
only_english_subs = english_subs.difference(french_subs)

# Print the total number of students with only English subscriptions
print(len(only_english_subs))


'''output :
Enter the number of English newspaper subscribers: 9
Enter the roll numbers of English subscribers: 1 2 3 4 5 6 7 8 9
Enter the number of French newspaper subscribers: 9
Enter the roll numbers of French subscribers: 10 1 2 3 11 21 55 6 8
4
'''