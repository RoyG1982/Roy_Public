import requests
import json
import concurrent.futures
from queue import Queue
import time
import socket
import datetime
import ssl

# Measure start time
start_time = time.time()

urls_queue = Queue()
analyzed_urls_queue = Queue()

# Load URLs into the queue
with open('20_domains.txt', 'r') as infile:
    for line in infile:
        urls_queue.put(line.strip())

print(f"Total URLs to check: {urls_queue.qsize()}")

# Define the URL checking function with a timeout and result storage
def check_url_liveness_and_cert():
    while not urls_queue.empty():
        url = urls_queue.get()
        result = {"url": url, "status_code": "", "expiry_status": "", "expiry_date": ""}  # Default to FAILED
        try:
            response = requests.get(f'http://{url}', timeout=1)
            if response.status_code == 200:
                result['status_code'] = 'OK'

            context = ssl.create_default_context()
            with socket.create_connection((url, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=url) as secure_sock:
                    cert = secure_sock.getpeercert()
            expiry_date = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            today = datetime.datetime.now()

            if expiry_date > today:
                result["expiry_status"] = "certificate is valid"
                result["expiry_date"] = str(expiry_date)
            else:
                result["expiry_status"] = "expired"
                result["expiry_date"] = str(expiry_date)

        except requests.exceptions.RequestException:
            result['status_code'] = 'FAILED'
            result["expiry_status"] = "Cert not obtained"
            result["expiry_date"] = "Cert not obtained"

        finally:
            analyzed_urls_queue.put(result)  # Add result to analyzed queue
            urls_queue.task_done()

# Generate report after all URLs are analyzed
def generate_report():
    results = []
    urls_queue.join()  # Wait for all URL checks to finish

    # Collect results from analyzed queue
    while not analyzed_urls_queue.empty():
        results.append(analyzed_urls_queue.get())
        analyzed_urls_queue.task_done()
    
    # Write results to JSON file
    with open('report.json', 'w') as outfile:
        json.dump(results, outfile, indent=4)
    print("Report generated in report.json")

# Run URL checks in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as liveness_threads_pool:
    # Submit URL check tasks
    futures = [liveness_threads_pool.submit(check_url_liveness_and_cert) for _ in range(20)]
    # Generate report after tasks complete
    liveness_threads_pool.submit(generate_report)

urls_queue.join()  # Ensure all URLs are processed

# Measure end time
end_time = time.time()
elapsed_time = end_time - start_time

print(f"URL liveness check complete in {elapsed_time:.2f} seconds.")