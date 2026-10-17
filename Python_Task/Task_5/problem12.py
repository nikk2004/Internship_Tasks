# 12. Capitalize
# Hackerank Link : https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

def solve(s):
    words = s.split(' ')
    
    capitalized_words = [word.capitalize() for word in words]
    
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    s = input("Enter a sentence: ")

    result = solve(s)

    print("Capitalized sentence:", result)


''' Output :
Enter a sentence: chris alan
Capitalized sentence: Chris Alan
'''