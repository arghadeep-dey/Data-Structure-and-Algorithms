'''
 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

#NestedLoop O(N^2):

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


#Two Pointers O(NlogN): 
'''
- original indices gets lost!! 
- need to store them in a tuple and sort based on the value
'''

def twoSum(nums, target):
    arr = [(num, i) for i, num in enumerate(nums)]
    arr.sort()
    
    left, right = 0, len(arr) - 1
    
    while left < right:
        curr_sum = arr[left][0] + arr[right][0]
        
        if curr_sum == target:
            return [arr[left][1], arr[right][1]]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


#HashMap O(N):

def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []