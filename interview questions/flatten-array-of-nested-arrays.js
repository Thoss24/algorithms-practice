Array.prototype.flatten = function () {
  let strArray = this.toString().split(",");

  return strArray.map((val) => Number(val));
};

const arr1 = [[1, [2]], [5]].flatten();
const arr2 = [[[1, 2], [3, [4, 5]], 6]].flatten();
//console.log(arr2)

Array.prototype.flatten2 = function () {

    const result = []

    for (const value of this) {
        if (Array.isArray(value)) {
            value.flatten2()
            result.push(flattened)
            console.log(result)
        } else {
            result.push(value)
        }
    }
    
    return result

};

//const arr4 = [[[1,2], [3, [4,5]], 6]].flatten2();
const arr5 = [[[1,2],[2, [7, [8]]], [3, [4,5]], 6]].flatten2();
//console.log(arr5)
