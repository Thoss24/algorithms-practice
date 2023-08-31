
const capitalizeEveryOtherChar = (str) => {

    let resultStr = ''

    for (const char in str) {
        if (char % 2 == 0) {
            let uppercase = str[char].toUpperCase();
            resultStr += uppercase
        } else
        resultStr += str[char];
    }

    return resultStr
}

console.log(capitalizeEveryOtherChar('hello world again again'));