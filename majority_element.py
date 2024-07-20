"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""


def majority_element(nums):
    N = len(nums)

    for num in nums:
        if count(num) > N / 2:
            return num
