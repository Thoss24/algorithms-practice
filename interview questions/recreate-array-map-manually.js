Array.prototype.myMap = function(cb) {

    const resultArr = []

    for (let i = 0; i < this.length; i++) {
        resultArr[i] = cb(this[i])
    }

    return resultArr
}

const arr = [1, 2, 3].myMap((val) => val * 2);
console.log(arr)