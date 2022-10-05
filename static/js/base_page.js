/*
    Logic for setting django messages
    to display none after 2secs - source idea:
    https://www.w3schools.com/jsref/prop_style_display.asp
*/

let message_flash = document.getElementById("message-flash");
setTimeout(function () {
    message_flash.style.display = "none";
}, 2000);
