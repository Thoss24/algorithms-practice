 
const findClosingTags = (str) => {
    // does the string have any spaces?
    // does the string start with a <div> tag?
    // what if it's an empty string with only the html tags?
    // will there be a space between the opening tag and the fist word

    let hasClosingTag = true

    let result = ''

    for (let i = 0; i < str.length; i++) {
        let iteratingStr = str.substring(i, str.length)

        let nextOpeningTag = iteratingStr.slice(0, 5);

        if (nextOpeningTag === '<div>' && hasClosingTag === true ) {
            hasClosingTag = false
            result += str[i]
            continue
        }

        if (nextOpeningTag === '<div>' && hasClosingTag === false) {
            result += str[i] + '/'
            hasClosingTag = true
        } else {
            result += str[i]
        }

    }

    return result
    
};

console.log(findClosingTags('<div><div><p>Hello</p><div><div><div><div>'))