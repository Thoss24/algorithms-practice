String.prototype.isPalindrome = function () {
    let reversedString = this.split("").reverse().join("");
    if (this.toString() === reversedString)  return true
    return false
};

let str = console.log("racecar".isPalindrome());