'''
 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

#NestedLoop O(N^2):
'''- brute force approach
- check every pair of numbers to see if they add up to the target
- time complexity: O(N^2)
- space complexity: O(1)
'''

def twoSumNL(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

#Example usage:
'''
nums = [2, 7, 11, 15]
target = 9
For loop 1: i = 0, j = 1, nums[0] + nums[1] = 2 + 7 = 9 == target, so we return [0, 1]
'''


#Two Pointers O(NlogN): 
'''
- sort the array and use two pointers to find the target sum
- original indices gets lost!! 
- need to store them in a tuple and sort based on the value
- time complexity: O(NlogN) due to sorting
- space complexity: O(N) due to storing the original indices in a new array
- Best for sorted arrays aas there time complexity is O(N) and space complexity is O(1)
'''

def twoSumTP(nums, target):
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

#Example usage:
'''
nums = [2, 7, 11, 15]
target = 9
arr = [(2, 0), (7, 1), (11, 2), (15, 3)]
left = 0, right = 3
curr_sum = 2 + 15 = 17 > target, so right -= 1
left = 0, right = 2
curr_sum = 2 + 11 = 13 > target, so right -= 1
left = 0, right = 1
curr_sum = 2 + 7 = 9 == target, so we return [arr[left][1], arr[right][1]] which is [0, 1]
'''

#HashMap O(N):
'''
- use a hash map to store the numbers and their indices
- for each number, check if the complement (target - current number) exists in the hash
- time complexity: O(N) due to single pass through the array
- space complexity: O(N) due to storing the numbers in the hash map
'''

def twoSumHM(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

#Example usage:
'''
nums = [2, 7, 11, 15]
target = 9
For loop 1: i = 0, num = 2, complement = 7
- complement 7 is not in num_map, so we add 2 to num_map with index 0: num_map = {2: 0}
For loop 2: i = 1, num = 7, complement = 2
- complement 2 is in num_map, so we return [num_map[2], 1] which is [0, 1]
'''