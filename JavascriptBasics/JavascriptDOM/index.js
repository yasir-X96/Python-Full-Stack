const heading = document.getElementById("heading");

console.log(heading);

console.log(heading.innerText);

const messages = document.getElementsByClassName("message");

console.log(messages);
console.log(messages[0].innerText);

console.log(messages[1].innerText);

const listItems = document.getElementsByTagName("li");

console.log(listItems);
const heading = document.querySelector("#heading");

console.log(heading.innerText);
//by class
const message = document.querySelector(".message");

console.log(message.innerText);
const heading2 = document.querySelector("h2");
//by tag
console.log(heading2.innerText);

const allMessages =
    document.querySelectorAll(".message");

console.log(allMessages);

allMessages.forEach(function (item) {

    console.log(item.innerText);

});