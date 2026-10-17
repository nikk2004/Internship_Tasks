# 15. Lists 
# Hackerrank Link : https://www.hackerrank.com/challenges/python-lists/problem

# Ask how many commands
n = int(input("Enter number of commands: "))

# Start with an empty list
arr = []

# Repeat for each command
for i in range(n):

    parts = input("Enter command: ").split()
    action = parts[0]

    if action == "insert":
        pos = int(parts[1])
        num = int(parts[2])
        arr.insert(pos, num)

    elif action == "append":
        num = int(parts[1])
        arr.append(num)

    elif action == "remove":
        num = int(parts[1])
        arr.remove(num)

    elif action == "print":
        print("List:", arr)

    elif action == "sort":
        arr.sort()

    elif action == "pop":
        arr.pop()

    elif action == "reverse":
        arr.reverse()


'''output : 
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1] '''