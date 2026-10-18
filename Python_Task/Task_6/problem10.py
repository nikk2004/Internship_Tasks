# 10. Designer Door Mat
# HackerRank Link : https://www.hackerrank.com/challenges/designer-door-mat/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read space-separated values for N and M from standard input
N, M = map(int, input().split())

# 1. Generate the Top Half of the Mat
# The pattern '.|.' starts at 1 and increases by 2 each row (1, 3, 5, ...)
for i in range(1, N, 2):
    print((".|." * i).center(M, "-"))

# 2. Generate the Center Row with 'WELCOME'
print("WELCOME".center(M, "-"))

# 3. Generate the Bottom Half of the Mat
# The pattern mirrors the top half, decreasing back to 1
for i in range(N - 2, 0, -2):
    print((".|." * i).center(M, "-"))

