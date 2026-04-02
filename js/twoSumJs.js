// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.
//Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


//NestedLoop O(N^2):
/*
- brute force approach
- check every pair of numbers to see if they add up to the target
- time complexity: O(N^2)
- space complexity: O(1)
*/

function twoSumNL(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }
    return [];
}

//Two Pointers O(NlogN): 
/*
- sort the array and use two pointers to find the target sum
- original indices gets lost!! 
- need to store them in a tuple and sort based on the value
- time complexity: O(NlogN) due to sorting
- space complexity: O(N) due to storing the original indices in a new array
- Best for sorted arrays aas there time complexity is O(N) and space complexity is O(1)
*/
function twoSumTP(nums, target) {
    let arr = nums.map((num, i) => [num, i]);
    
    arr.sort((a, b) => a[0] - b[0]); // sort by value
    
    let left = 0;
    let right = arr.length - 1;
    
    while (left < right) {
        let currSum = arr[left][0] + arr[right][0];
        
        if (currSum === target) {
            return [arr[left][1], arr[right][1]];
        } else if (currSum < target) {
            left++;
        } else {
            right--;
        }
    }
    
    return [];
}

//HashMap O(N):
/*
- use a hash map to store the numbers and their indices
- for each number, check if the complement (target - current number) exists in the hash
- time complexity: O(N) due to single pass through the array
- space complexity: O(N) due to storing the numbers in the hash map
*/
function twoSumHM(nums, target) {
    let hash = {};
    
    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i];
        
        if (hash.hasOwnProperty(complement)) {
            return [hash[complement], i];
        }
        
        hash[nums[i]] = i;
    }
    
    return [];
}