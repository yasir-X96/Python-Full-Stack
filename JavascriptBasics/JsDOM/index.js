const heading = document.getElementById("heading");
console.log(heading);
console.log(heading.innerText);

const message = document.getElementsByClassName("message")
console.log(message);
console.log(message[0].innerText);

const liItems=document.getElementsByTagName("li")
console.log(liItems);


const heading1=document.querySelector("#heading")
console.log(heading1.innerText);

const msg=document.querySelector(".message");
console.log(msg.innerText);


const allmsgs=document.querySelectorAll(".message")
console.log(allmsgs);

allmsgs.forEach(function(item){
    console.log(item.innerText);
    
})