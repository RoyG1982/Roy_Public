document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("URL_form").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form submission from reloading the page

        let url = document.getElementById("url").value; // Get the URL from the input field

        // Check if the URL is valid before sending
        if (!url) {
            document.getElementById("display_results").textContent = "Please enter a valid URL.";
            return;
        }

        // Send a GET request to check the URL liveness
        fetch(`/check_URL_liveness?url=${encodeURIComponent(url)}`)
            .then((response) => response.json())
            .then((data) => {
                // Display the URL status in the result div
                document.getElementById("display_results").textContent = data.message;
            })
            .catch((error) => {
                document.getElementById("display_results").textContent =
                    "Error checking URL: " + error;
            });
    });
});