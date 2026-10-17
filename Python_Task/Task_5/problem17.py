# 17. No idea
# Hackerank link : https://www.hackerrank.com/challenges/no-idea/problem

# Enter the size of the array and sets
n, m = map(int, input("Enter n and m: ").split())

# Enter array elements
arr = list(map(int, input("Enter array elements: ").split()))

# Enter elements of set A
A = set(map(int, input("Enter elements of set A: ").split()))

# Enter elements of set B
B = set(map(int, input("Enter elements of set B: ").split()))

happiness = 0

for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

print("Total happiness:", happiness)

''' Output : 
Enter n and m: 3 2
Enter array elements: 1 5 3
Enter elements of set A: 3 1
Enter elements of set B: 5 7
Total happiness: 1 '''