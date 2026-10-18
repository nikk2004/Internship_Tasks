# 18. Set Mutations
# Hackerrank Link : https://www.hackerrank.com/challenges/py-set-mutations/problem
# Read the number of elements in initial set A (not explicitly required for logic)
num_elements_A = int(input())

# Read the space-separated elements of set A
set_A = set(map(int, input().split()))

# Read the number of other sets/operations
num_operations = int(input())

# Process each operation block
for _ in range(num_operations):
    # Read the operation line and extract the operation name
    operation_info = input().split()
    operation_name = operation_info[0]
    
    # Read the elements of the mutating set
    other_set = set(map(int, input().split()))
    
    # Dynamically match and execute the structural mutation on set_A
    if operation_name == "update":
        set_A.update(other_set)
    elif operation_name == "intersection_update":
        set_A.intersection_update(other_set)
    elif operation_name == "difference_update":
        set_A.difference_update(other_set)
    elif operation_name == "symmetric_difference_update":
        set_A.symmetric_difference_update(other_set)

# Print the final sum of elements remaining in set A
print(sum(set_A))

'''output : 
38
'''