// ===============================
// SPAM X - app.js
// Smart Emergency Response System
// ===============================


// -------------------------------
// LOGIN FUNCTION
// -------------------------------

function loginUser(event){

    event.preventDefault();

    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    if(email === "" || password === ""){

        alert("❌ Please fill all fields!");
        return;

    }

    alert("✅ Login Successful!");

    window.location.href = "dashboard.html";

}



// -------------------------------
// REGISTER FUNCTION
// -------------------------------

function registerUser(event){

    event.preventDefault();

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let confirmPassword = document.getElementById("confirmPassword").value;

    if(name === "" || email === "" || password === ""){

        alert("❌ Please fill all fields!");
        return;

    }

    if(password !== confirmPassword){

        alert("❌ Passwords do not match!");
        return;

    }

    alert("✅ Registration Successful!");

    window.location.href = "login.html";

}



// -------------------------------
// SOS ALERT FUNCTION
// -------------------------------

function sendSOS(){

    alert("🚨 SOS Alert Sent Successfully!");

    console.log("Emergency Alert Activated");

}



// -------------------------------
// AMBULANCE REQUEST
// -------------------------------

function requestAmbulance(){

    alert("🚑 Ambulance Requested Successfully!");

    console.log("Ambulance Request Sent");

}



// -------------------------------
// BLOOD DONOR SEARCH
// -------------------------------

function searchDonor(){

    let bloodGroup = document.getElementById("bloodGroup").value;

    if(bloodGroup === ""){

        alert("❌ Please select blood group!");
        return;

    }

    alert("🩸 Searching donors for " + bloodGroup);

}



// -------------------------------
// LIVE LOCATION
// -------------------------------

function getLocation(){

    if(navigator.geolocation){

        navigator.geolocation.getCurrentPosition(showPosition);

    }else{

        alert("Geolocation is not supported!");

    }

}


function showPosition(position){

    let latitude = position.coords.latitude;
    let longitude = position.coords.longitude;

    console.log("Latitude: " + latitude);
    console.log("Longitude: " + longitude);

    alert("📍 Location Detected Successfully!");

}



// -------------------------------
// EMERGENCY CONTACT CALL
// -------------------------------

function callEmergency(number){

    window.location.href = "tel:" + number;

}



// -------------------------------
// HOSPITAL MAP
// -------------------------------

function openMap(){

    window.open("https://maps.google.com", "_blank");

}



// -------------------------------
// DARK MODE TOGGLE
// -------------------------------

function toggleDarkMode(){

    document.body.classList.toggle("dark-mode");

}



// -------------------------------
// LOADING SCREEN
// -------------------------------

window.onload = function(){

    console.log("✅ SPAM X System Loaded Successfully");

};



// -------------------------------
// EMERGENCY SOUND
// -------------------------------

function playAlertSound(){

    let sound = new Audio("sounds/alert.mp3");

    sound.play();

}



// -------------------------------
// AUTO DATE & TIME
// -------------------------------

function updateTime(){

    let now = new Date();

    let time = now.toLocaleTimeString();

    let clock = document.getElementById("clock");

    if(clock){

        clock.innerHTML = time;

    }

}


setInterval(updateTime, 1000);



// -------------------------------
// EMERGENCY STATUS
// -------------------------------

function updateEmergencyStatus(){

    let status = document.getElementById("status");

    if(status){

        status.innerHTML = "🟢 Emergency Services Active";

    }

}


updateEmergencyStatus();



// ===============================
// END OF FILE
// ===============================