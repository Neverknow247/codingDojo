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
    while (amount > 1) {
        p += 1;
        amount -= 1;
    }
    console.log("q= ", + q + ", d= " + d + ", n= " + n + ", p= " + p)
}
change(90)




function makeChangeWithDollars(cents) {
    var coins = {
        "dollars": [100, 0],
        "half dollars": [50, 0],
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
makeChangeWithDollars(90)