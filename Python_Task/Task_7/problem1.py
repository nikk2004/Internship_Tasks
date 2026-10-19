# 1. Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read English newspaper roll numbers
# hackerrank Link : https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

result = english.symmetric_difference(french)

print(len(result))

