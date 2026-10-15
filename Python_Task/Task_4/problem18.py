# 18. Lists

# 1. Ask the user how many commands they want to type
n = int(input("Enter the number of commands: "))

# 2. Start with an empty list
arr = []

# 3. Repeat the loop 'n' times for each command
for i in range(n):
    
    # Read the line and break it into pieces
    # Example: "insert 0 5" becomes ["insert", "0", "5"]
    parts = input("Enter the command: ").split()
    
    # The first piece is always the action name
    action = parts[0]
    
    # 4. Check what the action is and do it
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
        print(arr)
        
    elif action == "sort":
        arr.sort()
        
    elif action == "pop":
        arr.pop()
        
    elif action == "reverse":
        arr.reverse()

    
    
