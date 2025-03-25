document.addEventListener("DOMContentLoaded", function() {
    const upload_button = document.getElementById("upload_button");
    const fileInput = document.getElementById("add_txt_file");
    upload_button.addEventListener("click", () => fileInput.click());
    fileInput.addEventListener("change", handle_file_upload);
    
    // fetchAndDisplayDomains();
});

function handle_file_upload(e) {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const contents = e.target.result;
            const domains = contents.split('\n').filter(domain => domain.trim() !== '');
            
            fetch('/add_multiple', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ domains }),
                credentials: 'include'
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    document.getElementById("result").innerText = data.message;
                    fetchAndDisplayDomains();
                } else {
                    document.getElementById("result").innerText = `Error: ${data.message}`;
                }
            })
            .catch(error => {
                document.getElementById("result").innerText = "Error: " + error.message;
            });
        };
        reader.readAsText(file);
    }
}