# 3. Mutation
# HackerRank Link : https:https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


if __name__ == '__main__':
    s = input("Enter a string: ")
    i, c = input("Enter position and character: ").split()

    s_new = mutate_string(s, int(i), c)
    print("Modified string:", s_new)
    
''' Output :
Enter a string: abracadabra
Enter position and character: 5 k
Modified string: abrackdabra '''
