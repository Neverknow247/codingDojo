// Write a function that returns whether the given array has a balance point between indices, where one side’s sum is equal to the other’s. Example: [1,2,3,4,10] → true (between indices 4 & 10), but [1,2,4,2,1] → false.



function balance(arr) {
    sum1 = 0;
    sum2 = 0;
    for (j = arr.length - 1; j >= 0; j--) {
        sum2 += arr[j]
        console.log(sum2)
        for (i = 0; i < j; i++) {
            sum1 += arr[i];
        }
        if (sum1 == sum2) {
            console.log(i-1);
            console.log("true");
            return true;
        }
        sum1 = 0;
    }
    console.log("false");
    return false;
}

balance([1, 2, 2, 1, 5, 1])