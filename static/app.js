// Get references to the form and status elements
const form = document.getElementById('registration_form');
const statusDiv = document.getElementById('status');

// Add an event listener for form submission
form.addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from reloading the page

    // Get form data
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Send the data to the Flask server using Fetch API
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // Set the content type to JSON
        },
        body: JSON.stringify({ username, password })  // Send data as a JSON string
    })
    .then(response => response.json())  // Parse the JSON response
    .then(data => {
        // Display the server response
        if (data.message) {
            statusDiv.textContent = data.message;
            statusDiv.style.color = 'green';
        } else if (data.error) {
            statusDiv.textContent = data.error;
            statusDiv.style.color = 'red';
        }
    })
    .catch(error => {
        // Handle any errors during the fetch
        statusDiv.textContent = 'Error: ' + error.message;
        statusDiv.style.color = 'red';
    });
});
