const text = "Creative Developer | AI Enthusiast 🤖";
let i = 0;

function typing(){
if(i<text.length){
document.querySelector(".typing").innerHTML += text.charAt(i);
i++;
setTimeout(typing,50);
}
}

window.onload = typing;
