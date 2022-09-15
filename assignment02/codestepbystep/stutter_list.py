# https://www.codestepbystep.com/problem/view/python/recursion/stutter_list

# Write a recursive function named stutter_list that accepts a list of integers
# as a parameter and replaces every value in the list with two occurrences of
# that value. For example, suppose a list named s stores these values, from
# bottom => top:

# [13, 27, 1, -4, 0, 9]

# Then the call of stutter_list(s) should change the list to store the
# following values:

# [13, 13, 27, 27, 1, 1, -4, -4, 0, 0, 9, 9]

# Notice that you must preserve the original order. In the original list the 9
# was at the top and would have been popped first. In the new list the two 9s
# would be the first values popped from the list. If the original list is
# empty, the result should be empty as well.

# Constraints: Your solution must be recursive. Do not use any loops. Do not
# use any auxiliary collections or data structures to solve this problem.

def stutter_list(nums: list):
    if len(nums) == 0:
        return False
    t = nums.pop()
    stutter_list(nums)
    nums += 2 * [t]        # Appends t to nums twice
    return nums
    

# def stutter_list(nums: list):
#     try:
#         t = nums.pop()
#         stutter_list(nums)
#         nums += 2 * [t]        # Appends t to nums twice
#         return nums
#     except IndexError:
#         return False
    

s = [1, 2, 3]
print(stutter_list(s))    
    



