document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("feedback_form").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form submission from reloading the page

        let username = document.getElementById("username").value; // Get the username from the input field
        let email = document.getElementById("email").value; // Get the email from the input field
        let comment = document.getElementById("comment").value; // Get the comment from the input field

        // Email validation regex
        let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        // Validate email format
        if (!emailPattern.test(email)) {
            alert("Please enter a valid email address.");
            return;
        }
        
        // Send a GET request to check the URL liveness
        fetch(`/feedback?username=${encodeURIComponent(username)}&email=${encodeURIComponent(email)}&comment=${encodeURIComponent(comment)}`)

            .then((response) => response.json())
            .then((data) => {

                console.log(data)
                document.getElementById("display_results").textContent = "Thank you for your feedback";
            })
            .catch((error) => {
                document.getElementById("display_results").textContent =
                    "Error checking URL: " + error;
            });
    });
});