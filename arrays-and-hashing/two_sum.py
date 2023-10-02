
'''
    Given a list of integers A and an integer target, 
    return indices of the two numbers such that they add up to target.

    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    
    Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    
    Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
    
    time complexity: O(n), dict lookup is O(1)
    space complexity: O(n), dict size is O(n)
'''

def two_sum(nums: list[int], target: int) -> tuple:
    num_map = {} # initialise dictionary 
    
    for i in range(len(nums)): # iterate the list
        if target - nums[i] in num_map.keys(): # check if the complement is in the dict
            return i, num_map[target - nums[i]] # return the indices
        num_map[nums[i]] = i # add the number to the dict if complement not found
            
    