# 5. Write a function
# Hackerrank Link : https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    if year %400 ==0:
        return True
    elif year %100 == 0:
        return False
    elif year %4 == 0:
        return True
    else:
        return False
year = int(input("Enter a year: "))
print(is_leap(year))

'''output: 
Enter a year: 2026
False
'''