const arr = [2, 5, 1, 7, 3, 12, 35, 90, 54, 23];

const bubbleSort = () => {
    for (let i = 0; i < arr.length; ++i) { 
        console.log(arr[i] + " outer")
        for (let j = 0; j < arr.length - 1; ++j) { 
            console.log(arr[j] + " inner")
            if (arr[j] > arr[j + 1]) {
                let tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
            }
        }
    }
   
};
//bubbleSort()

const multiArr = [12, 3, 5, 4, 1, 8];

const multiplyAll = (arr) => {

    let product = 1

    for (let i = 0; i < arr.length; ++i) { // one iteration
        console.log(arr[i] + " I")
        for (let j = 0; j < arr.length; j++) { // j fully iterates for a single iteration of i 
            console.log(arr[j] + " J")
            for (let k = 0; k < arr.length; k++) { // k fully iterates for a single iteration of j 
                console.log(arr[k] + " K") // k fully iterates arr.length times i.e. full iteration 6 times for every single iteration of i
            }
            // product *= arr[i][j]
        }
    }

    return product
};

//multiplyAll(multiArr)
const nestedArr = [1, [3, 8, [4]], 5, [12, [5, [2]]]];

let result = 0

const addAllRecursion = (arr) => {

    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i])) {
            addAllRecursion(arr[i])
        } else {
            result += arr[i]                                                                  
        }
    }

    return 0

};

addAllRecursion(nestedArr) // 57600

