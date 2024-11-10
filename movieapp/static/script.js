document.addEventListener('DOMContentLoaded', function() {
    console.log('Page is loaded!')
    // Define all constants at the beginning
    const Spinner = document.getElementById('spinner');
    const CloseAnswer = document.querySelector('#close-answer');
    const Answer = document.querySelector('#answer');
    const Form = document.querySelector('form');
    const CityInput = document.querySelector('#name');

    // Function to toggle spinner visibility
    function spinner(flag) {
        console.log(`Spinner is toggled! with ${flag}`);
        // Spinner.style.display = flag ? 'block' : 'none';
        // same as 
        if (flag) { 
            Spinner.style.display = 'block'; 
        } else { 
            Spinner.style.display = 'none';
        }
    }

    // Close answer button event listener
    CloseAnswer.addEventListener('click', function() {
        Answer.style.display = 'none';
    });
    
    // Form submission event listener
    Form.addEventListener('submit', function(event) {
        console.log('Form is submitted!');
        event.preventDefault();

        // Display a message
        const city = CityInput.value;
        getWeather(city);
        console.log(`City: ${city}`);

        // Reset the form after submission
        event.target.reset();
    });

    // Function to get weather information
    async function movie_search(movie_name) {
        spinner(true);
        const response = await fetch(`/get_movie?movie=${movie_name}`);
        const data = await response.json();
        console.log(data);
        Answer.style.display = 'block';
        spinner(false);
        let counter = 0
        let list = ""
        for (let key in data) {
            if (key !== "Error") {
                counter += 1
                

            }


        }
    }
});
