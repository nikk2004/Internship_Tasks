# 19. Company Logo
# Hackerrank Link : https://www.hackerrank.com/challenges/most-commons/problem
from collections import Counter

if __name__ == '__main__':
    # Cleanly read the single line input string
    s = input().strip()
    
    # 1. Count frequencies using Counter(s)
    # 2. Sort by frequency descending (-x[1]) and alphabetically ascending (x[0])
    sorted_chars = sorted(Counter(s).items(), key=lambda x: (-x[1], x[0]))
    
    # Print exactly the top 3 most common characters
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")

'''output : 
aabbbccde
Expected Output
b 3
a 2
c 2
'''