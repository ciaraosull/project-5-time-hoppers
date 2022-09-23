/*
    Logic for Landing Page time 
    & image change
*/

// DOM Elements
const time = document.getElementById('time');

// Options
const showAmPm = true;

// Show Time & Update every second
function showTime() {
    let today = new Date(), hour = today.getHours(), min = today.getMinutes(), sec = today.getSeconds();

    // Set AM or PM on Clock depending on condition of hour
    const amPm = hour >= 12 ? 'PM' : 'AM';

    // Show 12hr Format for Clock
    hour = hour % 12 || 12;

    // Output Time
    time.innerHTML = `${hour}<span>:</span>${min}<span>:</span>${sec}`;

    setTimeout(showTime, 1000);
}

// Run
showTime();
