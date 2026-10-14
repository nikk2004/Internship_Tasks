# Q1. Find the Frequency of Each Word in a Sentence
def word_frequency(sentence):
    words = sentence.split()
    d = {}
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d


# Q2. Find the Frequency of Each Character in a Word
def character_frequency(word):
    frequency = {}
    for char in word:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1
    return frequency


# Q3. Find the First Non-Repeating Character in a Word
def first_count(word):
    list1 = []
    for char in word:
        if word.count(char) == 1:
            list1.append(char)
    if len(list1) == 0:
        return None
    else:
        return list1[0]


# Q4. Check Whether Two Strings Are Anagrams
def anagrams(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


# Q5. Find the First Repeating Character in a String
def first_repeating_character(string):
    s = set()
    for char in string:
        if char in s:
            return char
        else:
            s.add(char)
    return None


# Q6. Move All Zeros to the End of a List
def move_zeros(number):
    num = []
    for i in number:
        if i != 0:
            num.append(i)
    for i in number:
        if i == 0:
            num.append(i)
    return num 



# Q7. Find the Second Highest Distinct Number in a List
def second_highest(numbers):
    unique_numbers = sorted(set(numbers))
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[-2]



# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result


# Q9. Find the Missing Number from 1 to N
def find_missing_number(nums, n):
    total = n * (n + 1) // 2
    present_sum = sum(nums)
    return total - present_sum


# Q10. Find Two Numbers Whose Sum Equals a Target
def find_pair(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]

    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(nums):
    closest = nums[0]
    for num in nums:
        if abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest) and num > closest:
            closest = num
    return closest


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    result = []

    for num in list1:
        if num in list2 and num not in result:
            result.append(num)

    return result



# Q13. Rotate a List to the Right by K Positions
def rotate_right(nums, k):
    if len(nums) == 0:
        return []
    k = k % len(nums)
    return nums[-k:] + nums[:-k] if k != 0 else nums.copy()


# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_consecutive_sum(nums):
    max_sum = nums[0] + nums[1]

    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum



# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
def find_all_pairs(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = sorted([nums[i], nums[j]])

                if pair not in pairs:
                    pairs.append(pair)
    pairs.sort()
    return pairs






