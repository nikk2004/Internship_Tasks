# 5. String Validators
# HackerRank Link : https://www.hackerrank.com/challenges/string-validators/problem
if __name__ == '__main__':
    s = input("Enter a string: ")
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))

''' Output :
Enter a string: qA2
True
True
True
True
True'''