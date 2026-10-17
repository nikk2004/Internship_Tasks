#9. Set .add()
# Hackerank Link : https://www.hackerrank.com/challenges/py-set-add/problem
if __name__ == '__main__':
    n = int(input("Enter number of stamps: "))
    country_stamps = set()

    for _ in range(n):
        country = input("Enter country name: ")
        country_stamps.add(country)

    print("Number of distinct countries:", len(country_stamps))
    

''' Output :
Enter number of stamps: 7
Enter country name: UK
Enter country name: Chaina
Enter country name: USA
Enter country name: France
Enter country name: New Zealand
Enter country name: UK
Enter country name: France
Number of distinct countries: 5'''