function change(amount) {
    var q = 0;
    var d = 0;
    var n = 0;
    var p = 0;
    amount = amount;
    current = 0;
    while (current <= amount - 25) {
        q += 1;
        current += 25;
    }
    while (current <= amount - 10) {
        d += 1;
        current += 10;
    }
    while (current <= amount - 5) {
        n += 1;
        current += 5;
    }
    while (current < amount) {
        p += 1;
        current += 1;
    }
    console.log("q= ", + q + ", d= " + d + ", n= " + n + ", p= " + p)
}
change(90)