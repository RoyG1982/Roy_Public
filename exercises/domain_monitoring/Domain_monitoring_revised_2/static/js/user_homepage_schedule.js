document.addEventListener("DOMContentLoaded", function () {
    const schedule_button = document.getElementById("schedule_button");

    schedule_button.addEventListener("click", function () {
        let input_time = document.getElementById("input_schedule_time").value.trim();
        let response_element = document.getElementById("schedule_response");

        if (!input_time) { //check if empty, null, or undefined
            response_element.innerText = "Please enter a valid time.";
            return;
        }

        fetch('/schedule', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ "input_time": input_time })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                response_element.innerText = "Scheduled successfully. Monitoring will execute every " + input_time + " minutes";
            } else {
                response_element.innerText = "Scheduling was unsuccessful: " + data.message;
            }
        })
        .catch(error => {
            response_element.innerText = "Error: " + error.message;
        });
    });
});
