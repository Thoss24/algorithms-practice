Array.prototype.flatten = function () {
  let strArray = this.toString().split(",");

  return strArray.map((val) => Number(val));
};

const arr1 = [[1, [2]], [5]].flatten();
const arr2 = [[[1, 2], [3, [4, 5]], 6]].flatten();
//console.log(arr2)

Array.prototype.flatten2 = function () {

    let result = []

    const stripBrackets = (value) => {
        for (const val of value) {
            if (Array.isArray(val)) {
                stripBrackets(val)
            } else {
                result.push(val)
            }
        }
    }

    stripBrackets(this)
    
    return result

};

//const arr4 = [[[1,2], [3, [4,5]], 6]].flatten2();
const arr5 = [[[1,2],[2, [7, [8]]], [3, [4,5]], 6]].flatten2();
console.log(arr5)
