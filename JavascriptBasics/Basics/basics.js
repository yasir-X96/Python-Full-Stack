//variables
//const,var,let
//import { num1, num2, addNumbers, result } from './mathUtil.js'
// var studentName = "shree" //var is not block scoped
// {
//     var studentName = "vidhya"
//     console.log(studentName);

// }
// console.log(studentName);

// let pincode = 620014 //block scoped
// {
//     let pincode = 2000
//     console.log(pincode);

// }
// console.log(pincode);
// const PI = 3.414
// //PI=5
// console.log(PI);

// //DataTypes
// //Primitive Type---String, number,boolean,null, undefined,bigint,symbol
// //Reference Types---object array,function

// let empName = "shree"
// let age = 20
// let isEmployed = true;
// let salary;
// let manager = null

// console.log(typeof empName);
// console.log(typeof salary);
// console.log(typeof manager);


// //reference types
// let user =
// {
//     userName: "shree",
//     score: 2000

// }

// let skills = ["Js", "HTML", "CSS"]

// console.log(typeof user);
// console.log(typeof skills);
// console.log(Array.isArray(skills));
// // Functions
// //1 Function declaration
// //2. Function Expression
// // Arrow Function(Es6)

// //1.
// function addTwoNumbers(num1, num2) {
//     return num1 + num2
// }
// //2
// const subtract = function (num1, num2) {
//     return num1 - num2
// }

// //ArrowFunction
// const multiply = (num1, num2) => { return num1 * num2 }
// const multiply1 = (num1, num2) => num1 * num2

// console.log(addTwoNumbers(10, 10));
// console.log(subtract(10, 5));
// console.log(multiply(10, 10));

// //Arrow functions--used for callback
// const numbers = [1, 2, 3, 4]

// const changedArr = numbers.map(num => num * 2)
// console.log(numbers);
// console.log(changedArr);

// //object
// let employee = {
//     id: 200,
//     name: "shree",
//     dept: "IT",
//     isActive: true,
//     address: {
//         city: "Bangalore",
//         pincode: 89000,
//     },
//     getDetails() {
//         console.log(`Name is :: ${this.name} city::${this.address.city}`);

//     }
// }
// console.log(employee);
// //access specific fields
// console.log(employee.name);
// console.log(employee.address.city);
// employee.getDetails();
// //update object value
// employee.isActive = false
// //add a new property
// employee.role = "Trainer"
// console.log(employee);

// //loop
// Object.keys(employee).forEach((key) => {
//     console.log(key, ":", employee[key]);

// })

// //for in loop

// for (let emp in employee) {
//     console.log("employee", emp, "val::", employee[emp]);

// }

// //for of loop
// for (let num of numbers) {
//     console.log(num);

// }

// //built in methods of array
// let products = [
//     { id: 1, name: "Laptop", price: 60000 },
//     { id: 2, name: "Mobile", price: 50000 },
//     { id: 3, name: "Headphone", price: 6000 }
// ];
// //print names of products
// // for (i = 0; i < products.length; i++) {
// //     console.log(products[i].name)
// // }
// //map 
// let productNames = products.map((p) => p.name)
// console.log(productNames);

// //get all products whose price is greater or equal to 50000
// let filteredProducts = products.filter((p) => p.price >= 50000)
// console.log(filteredProducts);
// //get total price of all products

// let totalPrice = products.reduce((total, p) => total + p.price, 0)
// console.log(totalPrice);

// //find
// console.log(products.find((p) => p.id === 4));

// // name="101"
// // name1=101

// // if(name===name1){
// //     console.log("success");

// // }
// // else{
// //     console.log("fail");

// // }
// // Destructing
// //unpack values from array or objects into single variables--instead of accessing via property

// const employee1 = { name: "shree", age: 30, city: "Bangalore" }
// // object destructing
// const { name, city } = employee1
// console.log(name);
// console.log(city);
// //renaming while destructruing
// const { name: empName1 } = employee1
// console.log(empName);

// //destructure array
// const cities = ["Bangalore", "Mumbai", "Hyderabad"]
// const [first, second] = cities
// console.log(second);

// //destructure function parameters
// function printEmployee({ name, age }) {
//     console.log(`${name} is ${age} years old`);


// }

// printEmployee(employee1)

// //Spread and Rest Operators(...)
// //used to spreadout elements of an iterable object like array, map,set
// const odd = [1, 3, 5]
// const combined = [2, 4, 6, ...odd]
// console.log(combined);

// //rest operator
// function func(...input) {
//     let sum = 0;
//     for (let i of input) {
//         sum += i
//     }
//     return sum
// }
// console.log(func(10, 20))//30
// console.log(func(10, 20, 30))//60
// console.log(func(10, 20, 30, 40));//100

// //ternary operator
// //condition?valueIfTrue:valueIfalse

// const age1 = 20
// const canVote = age >= 18 ? "Cast vote" : "cannot cast vote"
// console.log(canVote);

// //logical and &&

// //Modules
// import { add } from "./mathUtil.js";

// //addNumbers()

// console.log(add(2, 5));//7

//Asynchronous --Promises and Async Await
//t1----started---completes
//t2-----cannot start--untill t1 completes---blocking application

//java script ---single thread, non-blocking operations
//promise, async await

//promise represents value--available now, later or never(error)--pending,fulfilled,rejected

//simpulating API Call

// function fetchUser(id){
//     return new Promise((resolve,reject)=>{
//         setTimeout(()=>{
//             if(id){
//                 resolve({id,name:"shree"});//suceess
//             }
//             else{
//                 reject("User id not provided")//failure
//             }
//         },3000);
//     });
// }

// fetchUser(1)
// .then((user)=>console.log("Fetched User",user))
// .catch((error)=>console.log("error",error))

//async and await

// async function getUser(){
//     try
//     {
//         const user=await fetchUser(1);
//         console.log("Fetched User ::",user);

//     }
//     catch(error){
//     console.log("error::",error);

//     }
// }
// getUser()

//Example --fetching data from  API
async function getPosts() {
    try {
        const response = fetch("https://jsonplaceholder.typicode.com/posts")
        const data = (await response).json();
        //const data= await response;
        console.log(data.slice(0, 2));//first two posts
        //console.log(data);

    }
    catch (error) {
        console.log("Failed to fetch records::", error);


    }
}
getPosts()

class Person{
    constructor(name,age){
        this.name=name;
        this.age=age;
    }

    greet(){
        console.log(`Welcome ${this.name}`);
        
    }
}

class Student extends Person{
    constructor(name,age,department){
        super(name,age)
        this.department=department
    }

}

const student=new Student("Shree",35,"IT")
student.greet()









