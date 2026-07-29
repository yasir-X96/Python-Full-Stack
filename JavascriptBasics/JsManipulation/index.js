function messageDisplay(){
    var text="<b>textchanged</b>"
    // document.getElementById("textToDisplay").innerText=text
    document.getElementById("textToDisplay").innerHTML = text
} 
//event listner
document.getElementById("displayText").addEventListener("click",()=>{
    var text = "<b>textchanged</b>"
    // document.getElementById("textToDisplay").innerText=text
    document.getElementById("textToDisplay").innerHTML = text
})

function changeImage(){
    document.getElementById("blackAndWhite").src ="./images/colour.jpg"
}

function changeFontSize(){
    document.getElementById("fontsize").style.fontSize="40px"
}