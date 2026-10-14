
from solutions import word_frequency
sentence = "python is easy and python is powerful"
result = word_frequency(sentence)
print("Q1 - Result:", result)


# Q2. Find the Frequency of Each Character in a Word
from solutions import word_frequency, character_frequency
print("Q2. Frequency of word:", character_frequency("banana"))


# Q3. Find the First Non-Repeating Character in a Word
from solutions import first_count
print("Q3. Non-Repeating Character:", first_count("swiss"))

# Q4. Check Whether Two Strings Are Anagrams
from solutions import anagrams
print("Q4. Anagram : ", anagrams("listen","silent"))


# Q5. Find the First Repeating Character in a String
from solutions import first_repeating_character
print("Q5. First Repeating Character:", first_repeating_character("programming"))


# Q6. Move All Zeros to the End of a List
from solutions import move_zeros
print("Q6. Moved Zeros:", move_zeros([0,1,2,0,4,0,5]))


# Q7. Find the Second Highest Number in a List
from solutions import second_highest
print("Q7 :", second_highest([10, 20, 40, 30, 40, 20]))


# Q8. Remove Duplicates
from solutions import remove_duplicates
print("Q8 :", remove_duplicates([1, 2, 3, 5, 6]))

# Q9. Find the Missing Number from 1 to N
from solutions import find_missing_number
print("Q9. ", find_missing_number([1, 2, 4, 5], 5))

# Q10. Find Two Numbers Whose Sum Equals a Target
from solutions import find_pair
print("Q10. ", find_pair([2, 7, 11, 15], 9))

# Q11. Find the Number Closest to Zero
from solutions import closest_to_zero
print("Q11. ", closest_to_zero([-8, -3, 2, 5, -2]))


# Q12. Find Common Elements Between Two Lists
from solutions import common_elements
print("Q12. ", common_elements([1, 2, 3, 4  ], [3, 4, 5, 6]))

# Q13. Rotate a List to the Right by K Positions
from solutions import rotate_right
print("Q13. ", rotate_right([1, 2, 3, 4, 5], 2))

# Q14. Find the Maximum Sum of Two Consecutive Elements
from solutions import max_consecutive_sum
print("Q14. ", max_consecutive_sum([1, 2, 3, 4, 5]))

# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
from solutions import find_all_pairs
print(find_all_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print(find_all_pairs([1, 2, 3, 4], 5))