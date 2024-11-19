// Get references to the forms and status element
const registrationForm = document.getElementById('registration_form');
const loginForm = document.getElementById('login_form');
const statusDiv = document.getElementById('status');

// Add event listener for the registration form
registrationForm.addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from reloading the page

    // Get form data for registration
    const username = document.getElementById('choose_username').value;
    const password = document.getElementById('choose_password').value;

    // Send the registration data to the Flask server using Fetch API
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

// Add event listener for the login form
loginForm.addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from reloading the page

    // Get form data for login
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Send the login data to the Flask server using Fetch API
    fetch('/login', {
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
            // Redirect or update the UI on successful login
            window.location.href = '/';  // Refresh page to show login status
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
