document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("searchButton").addEventListener("click", function () {
        let keyword = document.getElementById("keyword").value;
        let resultDiv = document.getElementById("movies");

        if (!keyword) {
            resultDiv.innerHTML = "<p>Please enter a movie name.</p>";
            return;
        }

        resultDiv.innerHTML = "<p>Loading...</p>";

        fetch(`/get_movies?keyword=${encodeURIComponent(keyword)}`) // example: converts "The Dark Knight" to "The%20Dark%20Knight"
            .then(response => response.json())  // Convert response to JSON
            .then(data => {
                console.log("Received JSON:", data);  // Debugging

                resultDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;  //$ allows you to embed expressions or variables inside a string.2 = indent, <pre> = to preserve spacing
                // JSON.stringify formats it nicely
            })
            .catch(error => {
                console.error("Error:", error);
                resultDiv.innerHTML = "<p>Error fetching movies.</p>";
            });
    });
});