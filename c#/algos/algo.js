// Write a function that returns whether the given array has a balance point between indices, where one side’s sum is equal to the other’s. Example: [1,2,3,4,10] → true (between indices 4 & 10), but [1,2,4,2,1] → false.

function balance(arr) {
    sum1 = 0;
    sum2 = 0;
    for (i = 0; i < arr.length; i++){
        sum1 += arr[i];
    }
}

balance([1, 2, 3, 4, 10])