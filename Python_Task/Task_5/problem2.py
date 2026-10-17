# 2. String Split and Join
# HackerRank Link : https://www.hackerrank.com/challenges/python-string-split-and-join/problem
def split_and_join(line):
    # write your code here
    words = line.split()
    result = "-".join(words)
    return result


if __name__ == '__main__':
    line = input("Enter a string: ")
    result = split_and_join(line)
    print(result)

'''
Output:
Enter a string: this is a string
this-is-a-string
'''