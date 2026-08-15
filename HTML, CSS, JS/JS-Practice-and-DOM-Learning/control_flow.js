//if

const isUserLoggedIn = true;
const temperature = 30;

if(2==="2"){
    console.log("Executed");
}

if(temperature > 50){
    console.log("Less than 50");
}
else{
    console.log("temperature is not less than 50");
}

const score=200;
if(score > 100){
    const power = "fly"
    console.log(`User power: ${power} `);
    //console.log("Score is greater than 100");
}
//console.log(`User power: ${power} `);

const balance = 1000;
if(balance > 500){
    console.log("Balance is greater than 500");
}

if (balance >500) console.log("Balance is greater than 500");


if (balance >500) console.log("Balance is greater than 500"),
console.log("This is the next line of code");

//if-else
if (balance > 500) {
    console.log("Balance is greater than 500");
}else if (balance < 500) {
    console.log("Balance is less than 500");
}   else {
    console.log("Balance is less than 1200");
}

const userLoggedIn = true;
const debitCard = true;
const LoggedInfromGoogle = false;
const LoggedInfromEmail = true;

if (userLoggedIn && debitCard) {
    console.log("Allow to buy courses");
}

if (LoggedInfromGoogle || LoggedInfromEmail) {
    console.log("User logged in");
}

//switch(key){
  //  case "value1":
    //    break;
//    case "value2":
  //      break;
    //default:
       // break;
//}

const month = 5;

switch(month){
    case 1: 
        console.log("January");
        break;  
    case 2: 
        console.log("February");        
        break;
    case 3: 
        console.log("March");
        break;
    case 4: 
        console.log("April");   
        break;
    case 5:
        console.log("May");
        break;
    case 6:
        console.log("June");
        break;  
    case 7:
        console.log("July");
        break;
    case 8:
        console.log("August");
        break;
    case 9:
        console.log("September");
        break;
    case 10:
        console.log("October");
        break;
    case 11:
        console.log("November");
        break;
    case 12:
        console.log("December");
        break;
    default:
        console.log("Invalid month");   
        break;
}

const userEmail="a@adima"

if(userEmail){
    console.log("Got User email");
}
else{
    console.log("No user email");
}

//falsy values in JavaScript
// false, 0, "", null, undefined, NaN, -0, BigInt 0n

// truthy values in JavaScript
// true, 1, "some string", [], {}, BigInt 1n, Infinity, "0", "false", "null", "undefined", function(){}

const EmptyObject = {};

if(Object.keys(EmptyObject).length === 0){
    console.log("Empty object is truthy");
}

false ==0; //true
false == ""; //true
0 == ""; //true

//Nullish Coalescing Operator (??) null udefined
let val1;
//val1 = 5 ?? 10; // 5
//val1 = val1 ?? 10; // 10
val1 = undefined ?? 10; // 10
console.log(val1);

// Ternary Operator
// condition ? expressionIfTrue : expressionIfFalse
const iceTeaPrice = 100;
iceTeaPrice < 50 ? console.log("Ice tea is cheap") : console.log("Ice tea is expensive");

//for

for (let i = 0; i < 10; i++) {
    const element = i;
    if(element==5){
        console.log("5 is best no.");
    }
    console.log(element)
}

for(let i = 0; i <= 10; i++) {
    console.log(`outer loop iteration: ${i}`);
    for (let j = 0; j <=10; j++) {
        //console.log(`inner loop iteration: ${j} and inner loop i: ${i}`);
        console.log(i + `*` + j + `=` + (i+j));
    }
}

let myArray = ["flash","batman","superman"];

for (let index = 0; index < myArray.length; index++) {
    const element = myArray[index];
    console.log(element);
}

//break & continue
for (let index = 1; index <= 20; index++) {
    if(index==5){
        console.log("Detected 5");
        break; // exits the loop when index is 5
    }
    console.log(index);
    
}
for (let index = 1; index <= 20; index++) {
    if(index==5){
        console.log("Detected 5");
        continue; // skips the current iteration when index is 5
    }
    console.log(index);
    
}

//while
let i = 0;  
while (i <= 10) {
    console.log(i);
    //i++;
    i = i + 2; // incrementing i by 2
}

let MyArr=["flash","batman","superman"];
let j = 0;
while (j < MyArr.length) {
    const element = MyArr[j];
    console.log(element);
    j++;
}

//do-while
let k = 0;  
do {
    console.log(k);
    k++;
} while (k <= 10);

let MyArr2=["flash","batman","superman"];
let l = 0;
do {
    const element = MyArr2[l];
    console.log(element);
    l++;
}
while (l < MyArr2.length);

//for-of
const superheroes = ["flash", "batman", "superman"];    
for (const hero of superheroes) {
    console.log(hero);
}

//Map
const myMap = new Map();
myMap.set("name", "John");
myMap.set("age", 30);
myMap.set("city", "New York");
for (const [key, value] of myMap) {
    console.log(`${key}: ${value}`);
}

//forin
const myObject = {
    name: "Adima",
    age: 19,
    city: "Aurangabad"
};
for (const key in myObject) {
        console.log(`${key}: ${myObject[key]}`);
}

//forEach
const myArray2 = ["apple", "banana", "cherry"];
myArray2.forEach((element, index) => {
    console.log(`Element at index ${index}: ${element}`);
});

myArray2.forEach(function(val){
    console.log(`Value: ${val}`);
    }
)

myArray2.forEach((val, index) => {
    console.log(`Value: ${val}, Index: ${index}`);
}
)


MyCoding=[
    {
        LanguageName: "JavaScript",
        Extension: ".js",
    },
    {
        LanguageName: "Java",
        Extension: ".java",
    },
    {
        LanguageName: "Python",
        Extension: ".py",
    }
]
MyCoding.forEach((val, index) => {
    console.log(`Language: ${val.LanguageName}, Extension: ${val.Extension}, Index: ${index}`);
});

const values= MyCoding.forEach((val, index) => {
    console.log(`Language: ${val.LanguageName}, Extension: ${val.Extension}, Index: ${index}`);
    return values;
});
console.log(values); // undefined, because forEach does not return a value

const MyNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const NewNums = MyNums.filter((num) => num>4);
console.log(NewNums); // [5, 6, 7, 8, 9, 10]

const NewNums2 =[];
MyNums.forEach((num) => {
    if(num > 4){
        NewNums2.push(num);
    }
});
console.log(NewNums2); // [5, 6, 7, 8, 9, 10]


const NewNums3 = MyNums
.map((num) => num * 10)
.map((num) => num + 1)
.filter((num) => num > 50);
console.log(NewNums3); // [51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151]

//Reduce
const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
console.log(sum); // 15
