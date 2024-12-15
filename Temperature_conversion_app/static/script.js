const result = document.getElementById('result_in_F');
const form = document.getElementById('result_form');
const input_temp = document.getElementById('temperature')

async function checkURL(url) {
    const response = await fetch(`/check_url?url=${url}`);
    const data = await response.json();
    console.log(data);
    console.log(data.status_code);
    status.textContent = `Status code: ${data.status_code}`;
}

form.addEventListener('submit', function(event) {
    console.log('Form is submitted!');
    result.textContent = (input_temp.value * 1.8 + 32)
    event.preventDefault();

})


// Temperature in degrees Celsius (°C) * 1.8) + 32