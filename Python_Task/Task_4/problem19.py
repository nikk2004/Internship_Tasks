# 19. Collections.Counter()

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
