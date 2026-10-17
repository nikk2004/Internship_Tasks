# 19. Merge the Tools!
# Hackerank Link : https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        part = string[i:i + k]
        result = ""

        for char in part:
            if char not in result:
                result += char

        print(result)


if __name__ == '__main__':
    string = input("Enter the string: ")
    k = int(input("Enter the value of k: "))
    merge_the_tools(string, k)


''' Output :
Enter the string: AABCAAADA
AB
CA
AD'''