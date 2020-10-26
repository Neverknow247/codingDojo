// function reverseString(stringInput) {

// }


// reverseString("hello")

// "olleh"


function reverse(str) {
    newstr =''
    for (i = str.length - 1; i >= 0; i--) {
        newstr += str[i]
    }
    console.log(newstr)
}

reverse('Hello World!');

function reverse(str){
    split = str.split("");
    rev = split.reverse();
    join = rev.join("");
    return join;
}
console.log(reverse('Hello World!2'));