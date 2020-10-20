// Get 1 to 255 - Write a function that returns an array with all the numbers from 1 to 255.

function oneToTwoFiveFive(){
    arr = [];
    for(i=1;i<=255;i+=1){
        arr.push(i);
    }
    return arr
}
oneToTwoFiveFive();
console.log(arr)

// Get even 1000 - Write a function that would get the sum of all the even numbers from 1 to 1000.  You may use a modulus operator for this exercise.

function evenOneThou(){
    sum = null;
    for(i=1;i<=1000;i+=1){
        if(i%2==0){
            sum+=i
        }
    }
    return sum
}
evenOneThou();
console.log(sum)

// Sum odd 5000 - Write a function that returns the sum of all the odd numbers from 1 to 5000. (e.g. 1+3+5+...+4997+4999).

function oddFiveThou(){
    sum = null;
    for(i=1;i<=5000;i+=1){
        if(i%2!=0){
            sum+=i;
        }
    }
    return sum
}
oddFiveThou();
console.log(sum);

// Iterate an array - Write a function that returns the sum of all the values within an array. (e.g. [1,2,5] returns 8. [-5,2,5,12] returns 14).

function iterArr(arr){
    var sum=null;
    for(i=0;i<arr.length;i+=1){
        sum+=arr[i];
    }
    return sum;
}
console.log(iterArr([1,2,3,4,5,6,7,8,9,10]));

// Find max - Given an array with multiple values, write a function that returns the maximum number in the array. (e.g. for [-3,3,5,7] max is 7)

function max(arr){
    var max = arr[0];
    for(i=0;i<arr.length;i++){
        if(max<arr[i]){
            max=arr[i];
        }
    }
    return max
}
console.log(max([7,3,8,4,3,9,40,29,42,32]))

// Find average - Given an array with multiple values, write a function that returns the average of the values in the array. (e.g. for [1,3,5,7,20] average is 7.2)

function average(arr){
    a=null;
    for(i=0;i<arr.length;i++){
        a+=arr[i];
    }
    return a/arr.length;
}
console.log(average([1,2,3,4,5,6,7,8,9,10]));

// Array odd - Write a function that would return an array of all the odd numbers between 1 to 50. (ex. [1,3,5, .... , 47,49]). Hint: Use 'push' method.

function odd(x,y){
    var arr = [];
    for(i=x; i<=y; i++){
        if(i%2!=0){
            arr.push(i);
        }
    }
    return arr
}
console.log(odd(1,50));

// Greater than Y - Given value of Y, write a function that takes an array and returns the number of values that are greater than Y. For example if arr = [1, 3, 5, 7] and Y = 3, your function will return 2. (There are two values in the array greater than 3, which are 5, 7).

function greaterThanY(arr,Y){
    var count = null;
    for(i=0;i<arr.length;i++){
        if(arr[i]>Y){
            count++;
        }
    }
    return count;
}
console.log(greaterThanY([1,2,3,4,5,6,7,8,9,10],7));

// Squares - Given an array with multiple values, write a function that replaces each value in the array with the value squared by itself. (e.g. [1,5,10,-2] will become [1,25,100,4])

function square(arr){
    for(i=0;i<arr.length;i++){
        arr[i]*=arr[i];
    }
    return arr;
}
console.log(square([1,2,3,4,5,6,7,8,9,10]));

// Negatives - Given an array with multiple values, write a function that replaces any negative numbers within the array with the value of 0. When the program is done the array should contain no negative values. (e.g. [1,5,10,-2] will become [1,5,10,0])

function negative(arr){
    for(i=0;i<arr.length;i++){
        if(arr[i]<0){
            arr[i] = 0;
        }
    }
    return arr;
}
console.log(negative([-5,-4,-3,-2,-1,0,1,2,3,4,5]));

// Max/Min/Avg - Given an array with multiple values, write a function that returns a new array that only contains the maximum, minimum, and average values of the original array. (e.g. [1,5,10,-2] will return [10,-2,3.5])

function maxMinAvg(arr){
    var max = arr[0];
    var min = arr[0];
    var avg = null;
    for(i=0;i<arr.length;i++){
        if(arr[i]<min){
            min = arr[i];
        }
        if(arr[i]>max){
            max = arr[i];
        }
        avg+=arr[i];
    }
    var newArr = [max, min, avg/arr.length]
    return newArr;
}
console.log(maxMinAvg([1,2,3,4,5,6,7,8,9,10]));

// Swap Values - Write a function that will swap the first and last values of any given array. The default minimum length of the array is 2. (e.g. [1,5,10,-2] will become [-2,5,10,1]).

function swapValue(arr){
    temp=arr[0];
    arr[0] = arr[arr.length-1];
    arr[arr.length-1] = temp;
    return arr;
}
console.log(swapValue([1,2,3,4,5]));

// Number to String - Write a function that takes an array of numbers and replaces any negative values within the array with the string 'Dojo'. For example if array = [-1,-3,2], your function will return ['Dojo','Dojo',2].

function numToString(arr){
    for(i=0;i<arr.length;i++){
        if(arr[i]<0){
            arr[i]="Dojo";
        }
    }
    return arr;
}
console.log(numToString([-5,-4,-3,-2,-1,0,1,2,3,4,5]));
