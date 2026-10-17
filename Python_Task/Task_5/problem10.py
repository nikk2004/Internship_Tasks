# 10.Swap case
# Hackerank Link : https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    a = ""
    for i in s:
        if i.isupper():
            a += i.lower()
        else:
            a += i.upper()
    return a

if __name__ == '__main__':
    s = input("Enter a string: ")
    result = swap_case(s)
    print("After swapping case:", result)
    

''' Output :
Enter a string: HackerRank.com presents "Pythonist 2".
After swapping case: hACKERrANK.COM PRESENTS "pYTHONIST 2". '''