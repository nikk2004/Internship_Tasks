# 20. Piling Up!
# Hackerank Link : https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

if __name__ == '__main__':
    t = int(input("Enter number of test cases: "))

    for _ in range(t):
        n = int(input("Enter number of cubes: "))
        cubes = deque(map(int, input("Enter cube sizes: ").split()))

        last = float('inf')

        while cubes:
            if cubes[0] >= cubes[-1]:
                current = cubes.popleft()
            else:
                current = cubes.pop()

            if current > last:
                print("No")
                break

            last = current
        else:
            print("Yes")


''' Output :
Enter number of test cases: 2
Enter number of cubes: 6
Enter cube sizes: 4 3 2 1 3 4
Yes
Enter number of cubes: 3
Enter cube sizes: 1 3 2
No '''