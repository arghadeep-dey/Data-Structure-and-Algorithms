// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.
//Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map={};
    for(let i=0;i< nums.length;i++){
        const complement = target - nums[i];
        if(map.hasOwnProperty(complement)){
            return[map[complement],i];
        }
        map[nums[i]]=i;
    }
    return[];
};