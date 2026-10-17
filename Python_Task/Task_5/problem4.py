# 4. Find a String
# HackerRank Link : https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count
    

if __name__ == '__main__':
    string = input("Enter a string: ")
    sub_string = input("Enter a substring: ")
    count = count_substring(string, sub_string)
    print(count)
    
'''
Output : 
Enter a string: ABCDCDC
Enter a substring: CDC
2
'''
