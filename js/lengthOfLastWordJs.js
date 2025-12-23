// Given a string s consisting of words and spaces, return the length of the last word in the string.

// A word is a maximal substring consisting of non-space characters only.

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let j = 0;
    let out = 0;
    for(let i=s.length; i>0;i--){
        if(s[i-1]!=" "){
            j++;
        }
        else if(s[i-1]==" " && j!=0){
            return j;
        }
    }
    return j;
};