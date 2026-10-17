# 8. Word Order
# Hackerrank Link : https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input("Enter number of words: "))
d = {}

for i in range(n):
    word = input("Enter a word: ")
    d[word] = d.get(word, 0) + 1

print("Number of distinct words:", len(d))
print("Frequency of each word:", *d.values())

''' Output :
Enter number of words: 4
Enter a word: bcdef
Enter a word: abcdefg
Enter a word: bcde
Enter a word: bcdef
Number of distinct words: 3
Frequency of each word: 2 1 1 '''