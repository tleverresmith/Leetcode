/**
 * @param {number} n
 * @return {string[]}
 */

var fizzBuzz = function (n) {
    retVal = []

    fizzDict = {
        3: 'Fizz',
        5: 'Buzz'
    }

    i = 1

    do {
        let value = ''
        for (key in fizzDict) {
            if (i % key === 0) {
                value += fizzDict[key]
            }
        }

        if (value.length === 0) {
            retVal.push(i.toString())
        } else {
            retVal.push(value)
        }

        i = i + 1
    } while (i <= n)

    return retVal
}