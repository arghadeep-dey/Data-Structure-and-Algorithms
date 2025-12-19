// Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    for(let i = 0; i <= haystack.length-needle.length; i++ ){
        if(haystack.substring(i,i+needle.length)==needle){
            return i;
            break;
        }
    }
    return -1;
};