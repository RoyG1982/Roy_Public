document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("searchButton").addEventListener("click", function() {
        fetch('/get_time')

    .then(response => response.json())
    .then(data => {
        document.getElementById("searchButton").textContent = "Current Time: " + data.time;

    })
    });
    
    });