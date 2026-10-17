# 16. Collection .Counter()
# Hackerrank Link : https://www.hackerrank.com/challenges/collections-counter/problem


from collections import Counter

n = int(input("Enter number of shoes: "))

sizes = list(map(int, input("Enter shoe sizes: ").split()))

shoe_count = Counter(sizes)

customers = int(input("Enter number of customers: "))

money = 0

for i in range(customers):
    size, price = map(int, input("Enter shoe size and price: ").split())

    if shoe_count[size] > 0:
        money += price
        shoe_count[size] -= 1

print("Total money earned:", money)


''' Output :
Enter number of shoes: 10
Enter shoe sizes: 2 3 4 5 6 8 7 6 5 18
Enter number of customers: 6
Enter shoe size and price: 6 55
Enter shoe size and price: 6 45
Enter shoe size and price: 6 55
Enter shoe size and price: 4 40
Enter shoe size and price: 18 60
Enter shoe size and price: 10 50
Total money earned: 200 '''