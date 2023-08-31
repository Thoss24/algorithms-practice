const formatQueryString = (str) => {
    // remove question mark from start of string & split each key value pair by amp
    const formattedStr = str.slice(1).split('&');
    // iterate through string & split each key value by the '=' 

    const queryObj = {}

    for (const pair of formattedStr) {
        let [key, value] = pair.split('=');

        if (!value) value = 'true';

        if (value || key) queryObj[key] = value;
    };
    // return object 

    return queryObj
};

console.log(formatQueryString('?foo=hello&bar=world&baz&maz&blue=bear&kaz'))


