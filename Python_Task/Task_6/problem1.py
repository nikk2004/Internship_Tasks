# if-else python
# Hackerrank Link : https://www.hackerrank.com/challenges/py-if-else/problem
n = int(input("Enter a number: "))
if n %2 == 1:
    print("Weird")
elif n>=2 and n<=5:
    print("Not Weird")
elif n>=6 and n<=20:
    print("Weird")
elif n >20:
    print("Not Weird")
    
'''output:
Enter a number: 4
Not Weird
'''