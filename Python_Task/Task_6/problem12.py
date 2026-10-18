# 12. Set .discard(), .remove() & .pop()
# Hackerrank Link : https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
# Read the number of elements in the set (not strictly required for processing, but part of input)
n = int(input("Enter the number of elements in the set: "))

# Read the space-separated elements and convert them into a set of integers
s = set(map(int, input("Enter the elements separated by spaces: ").split()))

# Read the number of commands to execute
num_commands = int(input("Enter the number of commands: "))

# Loop through and execute each command
for _ in range(num_commands):
    # Split the command input into a list (e.g., ['remove', '9'] or ['pop'])
    command_input = input("Enter command: ").split()
    command_name = command_input[0]
    
    if command_name == "pop":
        s.pop()
    elif command_name == "remove":
        val = int(command_input[1])
        s.remove(val)
    elif command_name == "discard":
        val = int(command_input[1])
        s.discard(val)

# Print the sum of the remaining elements in the set
print(sum(s))


'''output:
Enter the number of elements in the set: 9
Enter the elements separated by spaces: 1 2 3 4 5 6 7 8 9
Enter the number of commands: 4
Enter command: pop
Enter command: remove 9
Enter command: discard 1
Enter command: remove 2
15
'''