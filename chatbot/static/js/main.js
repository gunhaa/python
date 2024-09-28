
let chat = document.querySelector("#chat");
let client = document.querySelector("#client");
let server = document.querySelector("#server");
let chatbox = document.querySelector("#chatbox");


document.querySelector("#btn").addEventListener("click", e => {
    
    chatbox.insertAdjacentHTML("beforeend", `
    <div id="chatContext">
        <div id="client">${chat.value}</div>
    </div>`)
    
    fetch("/question", {
        method: "POST",
        headers: {
            "Content-Type" : "application/json"
        },
        body :JSON.stringify({
            "chat" : chat.value,
        }),
    })
    .then(response=> response.json())
    .then(data=>{
        chatbox.insertAdjacentHTML("beforeend", 
    `<div id="chatContext">
        <div id="server">${data.text}</div>
    </div>`)
    })
    .catch(()=>{
        
    })
    console.log(`눌러졌고 보낸메시지는 : ${chat.value}`)
})