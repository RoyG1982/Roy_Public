document.addEventListener("DOMContentLoaded", function() {
    const logout_button = document.getElementById("logout_button");
    logout_button.addEventListener("click", logout);

});

function logout() {
    fetch('/logout', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: name })
    })
    .then(response => {
        if (response.ok) {
            console.log("Logout successful");
            window.location.href = "/"; // Redirect after successful logout
        } else {
            console.error("Logout failed");
        }
    })
    .catch(error => console.error("Error:", error));
}
