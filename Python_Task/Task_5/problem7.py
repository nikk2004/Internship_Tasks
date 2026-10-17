# 7. Symmetric Difference
# HackerRank Link : https://www.hackerrank.com/challenges/symmetric-difference/problem
m = int(input("Enter size of set A: "))
a = set(map(int, input("Enter elements of set A: ").split()))

n = int(input("Enter size of set B: "))
b = set(map(int, input("Enter elements of set B: ").split()))

result = a.symmetric_difference(b)

print("Symmetric difference:")
for num in sorted(result):
    print(num)
    
''' Output : 
Enter size of set A: 4
Enter elements of set A: 2 4 5 9
Enter size of set B: 4
Enter elements of set B: 2 4 11 12
Symmetric difference:
5
9
11
12 '''