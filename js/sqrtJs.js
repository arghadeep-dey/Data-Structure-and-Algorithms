// Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

// You must not use any built-in exponent function or operator.

/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    if (x === 0) return 0;

    let r = x;
    while (r * r > x) {
        r = Math.floor((r + x / r) / 2);
    }
    return r;
};