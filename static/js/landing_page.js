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
    let today = new Date(), hour = today.getHours(), mins = today.getMinutes(), secs = today.getSeconds();

    // Set AM or PM on Clock depending on condition of hour
    const amPm = hour >= 12 ? 'PM' : 'AM';

    // Show 12hr Format for Clock
    hour = hour % 12 || 12;

    // Output Time
    time.innerHTML = `${hour}<span>:</span>${addZero(mins)}<span>:</span>${addZero(
        secs
    )} ${showAmPm ? amPm : ''}`;

    setTimeout(showTime, 1000);
}

// Add Zeros to 1 digit numbers in clock
function addZero(n) {
    return (parseInt(n, 10) < 10 ? '0' : '') + n;
}

// Set Background
function setBgImage() {
    let today = new Date(),
      hour = today.getHours();
  
    if (hour < 6) {
      // Morning
      document.body.style.backgroundImage = "url('https://res.cloudinary.com/ciara0s1980/image/upload/v1663962553/image1_wqtpf3.png')";

    } else if (hour < 12) {
        // Afternoon
        document.body.style.backgroundImage = "url('https://res.cloudinary.com/ciara0s1980/image/upload/v1663962562/image5_nr0pjn.png')";

    } else if (hour < 18) {
      // Afternoon
      document.body.style.backgroundImage = "url('https://res.cloudinary.com/ciara0s1980/image/upload/v1663962555/image2_x0y8yu.png')";

    } else {
      // Evening
      document.body.style.backgroundImage = "url('https://res.cloudinary.com/ciara0s1980/image/upload/v1663962553/image6_j8i8lf.png')";
      
      document.body.style.color = 'white';
    }
  }

// Run
showTime();
setBgImage();
