# 11. String Formatting
# Hackerrank Link : https://www.hackerrank.com/challenges/python-string-formatting/problem
def print_formatted(number):
    # Calculate the padding width based on the binary length of the maximum number
    width = len(bin(number)[2:])
    
    # Loop from 1 to number (inclusive)
    for i in range(1, number + 1):
        # Convert the number to decimal, octal, capitalized hex, and binary formats
        dec_val = str(i)
        oct_val = oct(i)[2:]
        hex_val = hex(i)[2:].upper()
        bin_val = bin(i)[2:]
        
        # Print each value right-aligned to the calculated width, separated by a space
        print(f"{dec_val.rjust(width)} {oct_val.rjust(width)} {hex_val.rjust(width)} {bin_val.rjust(width)}")

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print_formatted(n)
    

'''output :
Enter a number: 17
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
   '''
