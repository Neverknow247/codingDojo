function change(amount) {
    var q = 0;
    var d = 0;
    var n = 0;
    var p = 0;
    while (amount >= 25) {
        q += 1;
        amount -= 25;
    }
    while (amount >= 10) {
        d += 1;
        amount -= 10;
    }
    while (amount >= 5) {
        n += 1;
        amount -= 5;
    }
    while (amount >= 1) {
        p += 1;
        amount -= 1;
    }
    console.log("q= ", + q + ", d= " + d + ", n= " + n + ", p= " + p)
}
change(42)




function makeChangeWithDollars(cents) {
    var coins = {
        "dollars": [100, 0],
        // "half dollars": [50, 0],
        "quarters": [25, 0],
        "dimes": [10, 0],
        "nickels": [5, 0],
        "pennies": [1, 0]
    }
    for (key in coins) {
        while (cents >= coins[key][0]) {
            coins[key][1]++
            cents -= coins[key][0]
        }
    }
    console.log(cents + " cents can be represented by:")
    for (key in coins) {
        console.log(key + ": " + coins[key][1])
    }
}
makeChangeWithDollars(297)





function rollpercent(num) {
    arr = (roll(num));
    _min = arr[0],
        _max = arr[0],
        _avg = null;
    for (i = 0; i < arr.length; i++) {
        if (arr[i] < _min) {
            _min = arr[i];
        }
        if (arr[i] > _max) {
            _max = arr[i];
        }
        _avg += arr[i];
    }
    _avg = Math.round(_avg / arr.length);
    var newArr = [_max, _min, _avg]
    return ("Min: " + _min + " Max: " + _max + " Average: " + _avg);
}
function roll(num) {
    arr = [];
    count = 0;
    var last = null;
    for (i = 0; i < 500; i++) {
        var potato = Math.ceil(Math.random() * num);
        count++;
        arr.push(potato);
        if (last == potato) {
            console.log("Number of rolls: ", count);
            return arr
        }
        last = potato;
    }
    return arr;
}
console.log(rollpercent(20));


function rollStats() {
    var arr = [];
    for (i = 0; i < 4; i++) {
        var potato = Math.ceil(Math.random() * 6);
        arr.push(potato);
    }
    console.log(arr)
    var min = arr[3];
    for (i = 0; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i];
            temp = arr[i];
            arr[i] = arr[arr.length - 1];
            arr[arr.length - 1] = temp;
        }
    }
    // console.log(arr)
    arr.pop();
    var roll = null;
    for (i = 0; i < arr.length; i++) {
        roll += arr[i];
    }
    return roll;
}
console.log(rollStats());