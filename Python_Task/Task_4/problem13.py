# 13. Symmetric Difference

if __name__ == '__main__':
    n = int(input("Enter the number of elements in the first set: "))
    set1 = set(map(int, input("Enter the elements of the first set (space-separated): ").split()))
    m = int(input("Enter the number of elements in the second set: "))
    set2 = set(map(int, input("Enter the elements of the second set (space-separated): ").split()))
    
    symmetric_diff = sorted(set1.symmetric_difference(set2))
    for element in symmetric_diff:
        print(element)