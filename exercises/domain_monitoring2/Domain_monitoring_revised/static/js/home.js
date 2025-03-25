document.addEventListener("DOMContentLoaded", function() {
    let login_button = document.getElementById("login_button");
    login_button.addEventListener("click", function() {
        let name = document.getElementById("l_username").value;
        let password = document.getElementById("l_password").value;

        // Send login data to backend for verification
        fetch('/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: name, password: password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log("Login successful!");
                window.location.href = "/user_homepage"; // Redirect on successful login
            } else {
                console.log("Password incorrect.");
            }
        })
        .catch(error => {
            console.log("Error: " + error.message);
        });
    });

    let register_button = document.getElementById("register_button");
    register_button.addEventListener("click", function() {
        let name = document.getElementById("r_username").value;
        let password = document.getElementById("r_password").value;

        // Send registration data to backend
        fetch('/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: name, password: password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById("register_paragraph").innerText = "Registration successful!";
            } else {
                console.log(data.message); // Username exists or another issue
            }
        })
        .catch(error => {
            console.log("Error: " + error.message);
        });
    });
});
