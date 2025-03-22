document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("temp_conversion").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form submission from reloading the page

        let temp = document.getElementById("temp_c").value; // Get the temp from the input field
        let tempNumber = Number(temp); // Convert to a number

        // Validate input: check if it's actually a number
        if (temp === "" || isNaN(tempNumber)) {
            alert("Please enter a valid number for temperature.");
            return;
        }

        // Send a GET request to convert temp in C to temp in F
        fetch(`/temperature_conversion?temp_c=${encodeURIComponent(temp)}`)
            .then((response) => response.json())
            .then((data) => {
                console.log(data)
                // Display the converted temp in div
                document.getElementById("display_results").textContent = `Fahrenheit: ${data.fahrenheit}°F`;

            })
            .catch((error) => {
                document.getElementById("display_results").textContent =
                    "Error converting: " + error;
            });
    });
});