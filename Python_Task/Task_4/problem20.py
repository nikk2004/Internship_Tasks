# 20. No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input("Enter n and m: ").split())

arr = list(map(int, input("Enter array elements: ").split()))

A = set(map(int, input("Enter set A elements: ").split()))
B = set(map(int, input("Enter set B elements: ").split()))

happiness = 0

for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

print("Happiness:", happiness)