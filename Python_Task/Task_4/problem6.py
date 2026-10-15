# 6. Find the Runner-Up Score!

n = int(input("Enter number of scores: "))

scores = list(map(int, input("Enter scores: ").split()))

scores = list(set(scores))
scores.sort()

print("Runner-up score:", scores[-2])
