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


// Given a sorted array and a value, return whether the array contains that value. Do not sequentially iterate the array. Instead, ‘divide and conquer’, taking advantage of the fact that the array is sorted. As always, only use built-in functions that you are prepared to recreate (write yourself) on demand!


function search(arr, value){
    y = Math.floor((arr.length-1)/2)
    x = arr[y]
    count = 0
    console.log(y)
    console.log(x)
    while (x >= value){
        console.log('test')
        console.log(x)
        if(x == value){
            console.log("true")
            return true
        }
        if (y == 0){
            console.log("false")
            return false
        }
        for(i=0; i<count; i++){
            pass
        }
        y = Math.floor(y/2)
        console.log(y)
        x = arr[y]
        console.log(x)
    }
}
search([1,2,3,4,5,6], 1)