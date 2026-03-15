function sendMessage(){

let input=document.getElementById("userInput");

let message=input.value.trim();

if(message==="") return;

let chatbox=document.getElementById("chatbox");

chatbox.innerHTML+=`<div><b>You:</b> ${message}</div>`;

input.value="";

fetch("/chat",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
message:message
})

})

.then(response=>response.json())

.then(data=>{

chatbox.innerHTML+=`<div><b>AI:</b> ${data.reply}</div>`;

chatbox.scrollTop=chatbox.scrollHeight;

})

.catch(error=>{

chatbox.innerHTML+=`<div><b>AI:</b> Server not responding.</div>`;

});

}