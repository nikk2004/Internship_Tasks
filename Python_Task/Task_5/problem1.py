# Q1. RUnner up 
# HackerRank Link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input("Enter number:"))

    scores = list(map(int, input("Enter scores separated by space: ").split()))

    scores = list(set(scores))
    scores.sort()

    print(scores[-2])
    
''' Output : Enter number:5
Enter scores separated by space: 2 3 6 6 5
5'''