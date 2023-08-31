 
const findClosingTags = (str) => {
    // does the string have any spaces?
    // does the string start with a <div> tag?
    // what if it's an empty string with only the html tags?

    let result = '';

    for (let char = 0; char < str.length; char++) {

        let segmentedStr = str.slice(char, str.length);

        let endOfString = segmentedStr.substr(segmentedStr.length - 5);

        let nextOpeningTag = segmentedStr.slice(0, 5);

        if (nextOpeningTag === '<div>') {
            result[char] += '</div>'
            console.log(result[char])
        } else result += str[char]

        if (endOfString === '</div>') return

        //console.log(endOfString)

    }

    //console.log(result)
    
};

findClosingTags('<div>hello world <div>find the closing tag')