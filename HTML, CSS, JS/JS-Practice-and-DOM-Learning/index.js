console.log("Hello, Adima!");

var a = 5;
var b = 6;
var ans = a + b;
console.log(ans);


let x = 10;
let y = 20;
let result = x * y;
const z = 30;
console.log(result);

myArray = [1, 2, 3, 4, 5];
myArray.push(6);
console.log(myArray);

// Displaying the results in a table format
console.table([myArray, ans, result]);

let person;
// JavaScript will give us person as undefined but it will store the value as undefined

let m = null;
// JavaScript will give us x as null but it will store the value as null
// Type of null is object in JavaScript

console.log(typeof person); // undefined
console.log(typeof m); // object
console.log(typeof null); // object
console.log(typeof undefined); // undefined

let score = 33;
console.log(typeof(score)); 

let valueInNumber = Number(score);
console.log(typeof(valueInNumber)); 
//"33" = 33
//true = 1
//false = 0
// NaN = Not a Number
// "undefined" = NaN
// 33abc = NaN

let isLoggedIn = 1;

let BooleanisLoggedIn = Boolean(isLoggedIn);
//console.log(Boolean(isLoggedIn)); 
console.log(BooleanisLoggedIn);

//0=false, 1=true, ""=false, " some string " = true, null=false, undefined=false, NaN=false

let myString = "Hello, World!";

let myStringConversion = String(myString);
console.log(myStringConversion);
console.log(typeof(myStringConversion)); // string


//****************Operations******************/

let value = 3; 
let NegValue = -value; // Negation
console.log(NegValue); // -3

let value1="Adima";
let value2=" Zareen";
let value3 = value1 + value2; // Concatenation
console.log(value3); // Adima Zareen

console.log("1"+2); // "12" (string concatenation)
console.log(1+2); // 3 (number addition)
console.log("1" + 2 + 3); // "123" (string concatenation)
console.log(1 + 2 + "3"); // "33" (number addition followed by string concatenation)
console.log(1 + "2" + 3); // "123" (number addition followed by string concatenation)
console.log("1" + (2 + 3)); // "15" (string concatenation with parentheses)

let gameCounter = 100;
console.log(gameCounter++); // 100 (post-increment, returns the value before incrementing)
console.log(++gameCounter); // 101 (pre-increment, returns the value after incrementing)

//Dates
let currentDate = new Date();
console.log(currentDate); // Current date and time
console.log(currentDate.toString()); // String representation of the current date
console.log(currentDate.toISOString()); // ISO format of the current date

let myTimeStamp = Date.now();
console.log(myTimeStamp); // Current timestamp in milliseconds since January 1, 1970
