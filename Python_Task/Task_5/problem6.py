# 6. Introduction to Sets
# Hackerank Link : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    unique_elements = set(array)
    return sum(unique_elements) / len(unique_elements)


if __name__ == '__main__':
    n = int(input("Enter number of plants: "))
    arr = list(map(int, input("Enter plant heights: ").split()))

    result = average(arr)
    print("Average height:", round(result, 3))


''' Output :
Enter number of plants: 10
Enter plant heights: 161 182 161 154 176 170 167 171 170 174
Average height: 169.375 '''