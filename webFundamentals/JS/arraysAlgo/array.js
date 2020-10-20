var testArr = [6,3,5,1,2,4]
var sum = null
for(i=0;i<testArr.length;i+=1){
    num=testArr[i]
    sum+=testArr[i]
console.log("Num "+ num +", " + "Sum " + sum)
}


var testArr = [6,3,5,1,2,4]
for(i=0;i<testArr.length;i+=1){
    testArr[i] *= i
}
console.log(testArr)