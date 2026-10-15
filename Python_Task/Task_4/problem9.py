# 9. Mutations

def mutate_string(string, position, character):
    return string[:position]+ character + string[position+1:]

if __name__ == '__main__':
    s = input("Enter a string: ")
    i, c = input("Enter the position and character : ").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)