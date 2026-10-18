# 20. Validating phone numbers
# Hackerrank Link : https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

# Read the total number of inputs
n = int(input())

# Compile the regular expression pattern for a valid mobile number:
# ^     : Assures the match begins at the start of the string
# [789] : Matches exactly one digit that is a 7, 8, or 9
# \d{9} : Matches exactly 9 decimal digits following the first character
# $     : Assures the match ends exactly at the final character (ensures exactly 10 digits total)
mobile_pattern = re.compile(r"^[789]\d{9}$")

# Process each input string
for _ in range(n):
    string_to_check = input().strip()
    
    # Check if the string matches the compiled expression
    if mobile_pattern.match(string_to_check):
        print("YES")
    else:
        print("NO")

'''output : 
Input (stdin)
2
9587456281
1252478965
Expected Output
YES
'''
