document.addEventListener('DOMContentLoaded', function() {

console.log('JavaScript loaded')

const currentDate = new Date();

const hours = currentDate.getHours();
const minutes = currentDate.getMinutes();

const button = document.getElementById('time_button');

time_button.addEventListener('click', function() {
    button.textContent = (`Current Time: ${hours}:${minutes}`)
    });

 })