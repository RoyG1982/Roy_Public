document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("calculation_form").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form submission from reloading the page

        let input_number_1 = document.getElementById("input_number_1").value; // Get the input_number from the input field
        let input_number_2 = document.getElementById("input_number_2").value; // Get the input_number from the input field
        let arithmetic_operation = document.getElementById("arithmetic_operation").value; // Get the arithmetic_operation from the input field

        // Send a GET request for the input_number and arithmetic operation
        fetch(`/calculate?input_number_1=${encodeURIComponent(input_number_1)}&input_number_2=${encodeURIComponent(input_number_2)}&arithmetic_operation=${encodeURIComponent(arithmetic_operation)}`)

            .then((response) => response.json())
            .then((data) => {
                console.log(data)
            })

            .catch((error) => {
                document.getElementById("display_results").textContent =
                    "Error converting: " + error;
            });
    });
});