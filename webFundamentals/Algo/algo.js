// Print numbers 1-5
// Print out all the numbers from 1 to 5 in order

// Physical: Hold up my hand with 1 finger up (so starting at 1)
// Code: Starting a for loop with a loop number that begins at 1
// Physical: Hold up one finger at a time until there are no fingers left ( usually 5 )
// Code: Every loop, console log the number until we get to the last number (usually 5)
// Physical: I know I am done when I have held up 5 fingers
// Code: Make sure to only loop if the number is less than or equal to 5

// ---------------------------------------------------------------------------

// Print odds 1-20
// Print out all odd numbers from 1 to 20 (odd numbers will give you a remainder if you divide them by 2)
// There are TWO solutions for this one, and one DOESN'T use modulo (%)
// The expected output will be 1, 3, 5, 7, 9, 11, 13, 15, 17, 19

// Break it down into pseudocode first
// Write actual code after

// ---------------------------------------------------------------------------


// Sum and Print 1-5
// Sum numbers from 1 to 5, printing out the current number and sum so far at each step of the way
// So add up 1 + 2 + 3 + 4 + 5
// The expected output will be: Num: 1, Sum: 1, Num: 2, Sum: 3, Num: 3, Sum: 6, Num: 4, Sum: 10, Num: 5, Sum: 15

// Break it down into pseudocode first
// Write actual code after


for(i=1; i<=5; i+=1){
    console.log(i)
}

for(i=1; i<=20; i+=2){
    console.log(i)
}

for(i=1; i<=20; i+=1){
    if(i % 2 == 1){
        console.log(i)
    }
}
var sum = 0
for(i=1; i<=5; i+=1){
    sum+=i
    console.log("Num: " + i)
    console.log("Sum: " + sum)
}