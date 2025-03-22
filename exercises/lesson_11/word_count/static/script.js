document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("word_count_form").addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form submission from reloading the page

        let text_input = document.getElementById("text_input").value; // Get the text input from the input field
        
        // Send a GET request to count words
        fetch(`/word_count?text_input=${encodeURIComponent(text_input)}`)

            .then((response) => response.json())
            .then((data) => {

                console.log(data)
                document.getElementById("display_results").textContent = "Word count: " + data["number_of_words"];
            })
            .catch((error) => {
                document.getElementById("display_results").textContent =
                    "Error checking URL: " + error;
            });
    });
});