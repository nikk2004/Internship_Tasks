# 17. Check Strict Superset
# Hackerrank Link : https://www.hackerrank.com/challenges/py-check-strict-superset/problem
# Read the main set A
set_A = set(map(int, input().split()))

# Read the number of other sets to check against
num_other_sets = int(input())

# Assume true until a violation is found
is_strict_superset = True

# Check each of the N sets
for _ in range(num_other_sets):
    other_set = set(map(int, input().split()))
    
    # Check if set_A is a strict superset of other_set
    # A set is a strict superset if it contains all elements of the other set
    # AND is strictly larger than the other set.
    if not (set_A.issuperset(other_set) and len(set_A) > len(other_set)):
        is_strict_superset = False
        break

# Print the final result
print(is_strict_superset)


'''output : 
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
False
'''