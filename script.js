function joinNow() {
    alert("Welcome to Gym Fitness!");
    window.location.href = "/register";
}

function changeMode() {

    document.body.classList.toggle("light-mode");

    let button = document.getElementById("mode-btn");

    if (document.body.classList.contains("light-mode")) {
        button.innerHTML = "Dark Mode";
    } else {
        button.innerHTML = "Light Mode";
    }
}

function sendMessage() {

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let message = document.getElementById("message").value;

    if (name == "" || email == "" || message == "") {
        alert("Please fill all fields.");
        return false;
    }

    alert("Thank you " + name + "! Your message has been sent successfully.");

    document.getElementById("contactForm").reset();

    return false;
}