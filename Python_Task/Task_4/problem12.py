# 12. Introduction to Sets

if __name__ == '__main__':
    n = int(input("Enter the no. of elements: "))
    elements = list(map(int, input("Enter the elements: ").split()))
    unique_elements = set(elements)
    print(sum(unique_elements) / len(unique_elements))