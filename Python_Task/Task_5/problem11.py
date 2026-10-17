# 11. Text Wrap
# Hackerrank Link : https://www.hackerrank.com/challenges/text-wrap/problem
import textwrap

def wrap(string, max_width):
    result = ""
    for i in range(0, len(string), max_width):
        result += string[i:i + max_width] + "\n"
    return result

if __name__ == '__main__':
    string = input("Enter a string: ")
    max_width = int(input("Enter maximum width: "))

    result = wrap(string, max_width)
    print("Wrapped string:")
    print(result)
    

''' Output :
Enter a string: ABCDEFGHIJKLIMNOQRSTUVWXYZ
Enter maximum width: 4
Wrapped string:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
  '''
