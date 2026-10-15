# 15. Word order

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input("Enter the number of words: "))
d = {}
for i in range(n):
    word = input("Enter a word: ")
    d[word] = d.get(word,0)+1
    
print(len(d))
print(*d.values())