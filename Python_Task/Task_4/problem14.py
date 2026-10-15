# 14. Set .add()

if __name__ == '__main__':
    n = int(input("Enter the no. of country stamps: "))
    country_stamps = set()
    for _ in range(n):
        country = input("Enter the no. of country: ")
        country_stamps.add(country)
    print(len(country_stamps))
