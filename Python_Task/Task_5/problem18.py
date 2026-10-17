# 18. MIni game
# Hacker rank Link : https://www.hackerrank.com/challenges/the-minion-game/problem


def minion_game(string):
    vowels = "AEIOU"
    kevin = 0
    stuart = 0

    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input("Enter the string: ")
    minion_game(s)


''' Output :
Enter the string: BANANA
Stuart 12 '''