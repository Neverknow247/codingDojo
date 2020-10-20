
var sum = 0;


function oddSum() {
    for (i = 1; i <= 5000; i++) {
        if (i % 2 != 0) {
            sum += i;
        }
    }
    return sum;
}

var y = oddSum()
console.log(y)

// Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).

function greaterY(arr, Y) {
    for (i = 0; i < arr.length; i++) {
        if (arr[i] > Y) {

        }
    }
    return count;
}


function reverse(arr) {
    if (arr == null) {
        return "NOPE"
    }
    else {
        for (var i = 0; i < arr.length / 2; i++) {
            temp = arr[i]
            arr[i] = arr[arr.length - 1 - i]
            arr[arr.length - 1 - i] = temp
        }
        return arr
    }
}

console.log(reverse([3, 1, 6, 4, 2]))

function reverse(arr) {
    arr.reverse();
    return arr
}
console.log(reverse([3, 1, 6, 4, 2]))

var object1 = "string"