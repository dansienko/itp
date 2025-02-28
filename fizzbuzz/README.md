# itp
 the first thing I did was open up our class repository and check out the code along from last class
 found some good stuff, I am able to print numbers divisible by 7 and 5 between 1 and 100. Now I need to find out how to print all numbers 1-100 and replace the ones divisible with words.
 
 Before I go further, I am going to see what ChatGPT can do for me. I'm gonna try literally copying the assignment prompt and seeing what it does.

 I said "How do I Write a JavaScript program that prints all the integers between 1 and 100, except in three situations:

If an integer in the counter is divisible by 3, print "Fizz";

if an integer in the counter is divisible by 5, print "Buzz";

if an integer in the counter is divisible by both 3 and 5, print "FizzBuzz"."

I recived this code
'for (let i = 1; i <= 100; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
        console.log("FizzBuzz");
    } else if (i % 3 === 0) {
        console.log("Fizz");
    } else if (i % 5 === 0) {
        console.log("Buzz");
    } else {
        console.log(i);
    }
}'
Let's see if it works in the code sandbox
It works! Now to throw it in fizzbuzz.js and call it a day. Thanks AI, I'll never think again!