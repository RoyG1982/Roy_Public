const Form = document.getElementById('check-form');
const status = document.getElementById('status');
const paragraph = document.getElementById("error_message");

Form.addEventListener('submit', function(event) {
    console.log('Form is submitted!');
    event.preventDefault();
    const url = document.getElementById('url').value; 
    console.log(`URL: ${url}`);
    paragraph.textContent = "";

    function separateAfterLastDot(url) {
    // Find the index of the last dot
    const lastDotIndex = url.lastIndexOf('.');

    after_dot = url.slice(lastDotIndex + 1);

        const list = ["com", "org", "net", "edu"];
        const searchString = after_dot;

        if (list.includes(searchString)) {
        console.log("No error");

        } else {
            paragraph.textContent = "URL must contain .com/.org/.net/.edu";
        }

    }
    
    // Example usage
    const inputString = url;
    const result = separateAfterLastDot(inputString);
    console.log(result);  // Output: "extension"

    checkURL(url);
});

async function checkURL(url) {
    const response = await fetch(`/check_url?url=${url}`);
    const data = await response.json();
    console.log(data);
    console.log(data.status_code);
    status.textContent = `Status code: ${data.status_code}`;
}