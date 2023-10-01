
"""
    Give an array of integers return true if the array contains any duplicates
    Solution: Use a set() to keep track of the numbers already visited.
    The set has a O(1) lookup time.
    The time complexity is O(n) since we have to iterate through the entire array.
    The space complexity is O(n) since we have to store all the numbers in the set.
"""
def solution(nums: list[int]) -> bool:
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
