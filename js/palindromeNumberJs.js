//Given an integer x, return true if x is a palindrome, and false otherwise.
//Could you solve it without converting the integer to a string?

/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let z = x;
    let y = 0;
    while (z>0){
        y=y*10 + z%10;
        z=Math.floor(z/10);
    }
    if(y==x)return true;
    else return false;
};