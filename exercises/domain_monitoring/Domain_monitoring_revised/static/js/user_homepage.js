document.addEventListener("DOMContentLoaded", function() {
    const logout_button = document.getElementById("logout_button");
    const check_button = document.getElementById("check_button");
    const add_button = document.getElementById("add_button");
    const upload_button = document.getElementById("upload_button");
    const fileInput = document.getElementById("add_txt_file");

    logout_button.addEventListener("click", logout);
    check_button.addEventListener("click", check_domain);
    add_button.addEventListener("click", add_domain);
    upload_button.addEventListener("click", () => fileInput.click());
    fileInput.addEventListener("change", handle_file_upload);

    fetchAndDisplayDomains();
});

function check_domain() {
    const domain = document.getElementById("domain").value;
    fetch('/check', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `domain=${domain}`,
        credentials: 'include'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = data.result;
        if (data.cert_info) {
            document.getElementById("result").innerHTML += `<br>Common Name: ${data.cert_info[0]}<br>Valid Until: ${data.cert_info[1]}`;
        }
    })
    .catch(error => {
        document.getElementById("result").innerText = "Error: " + error.message;
    });
}

function add_domain() {
    const domain = document.getElementById("domain").value;
    fetch('/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `domain=${domain}`,
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
}

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

function fetchAndDisplayDomains() {
    fetch('/get_domains')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                const domainsList = document.getElementById('domains-list');
                domainsList.innerHTML = ''; // Clear existing content
                data.domains.forEach(domain => {
                    const domainElement = document.createElement('div');
                    domainElement.className = 'domain-item';
                    domainElement.innerHTML = `
                        <span>${domain.domain}</span>
                        <span>${domain.liveness}</span>
                    `;
                    if (domain.cert_info) {
                        domainElement.innerHTML += `
                            <span>Common Name: ${domain.cert_info[0]}</span>
                            <span>Valid Until: ${domain.cert_info[1]}</span>
                        `;
                    }
                    domainsList.appendChild(domainElement);
                });
            } else {
                console.error('Failed to fetch domains:', data.message);
            }
        })
        .catch(error => console.error('Error:', error));
}

function logout() {
    fetch('/logout', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: name })
    })
    .then(response => {
        if (response.ok) {
            console.log("Logout successful");
            window.location.href = "/"; // Redirect after successful logout
        } else {
            console.error("Logout failed");
        }
    })
    .catch(error => console.error("Error:", error));
}
