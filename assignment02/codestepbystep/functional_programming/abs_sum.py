import functools

def abs_sum(nums: list):
    return sum(map(abs, nums))


#Test Case
nums = [-1, 2, -4, 6, -9]
print(abs_sum(nums))
    