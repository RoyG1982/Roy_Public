import threading
import schedule
import time

scheduler_running = False  # Flag to check if the scheduler is running

# Function that runs the scheduled job
def job():
    print("I'm working...")

# Function to run the scheduler in a background thread
def run_scheduler():
    print("Scheduler thread started!")  # Debugging print
    while True:
        schedule.run_pending()
        print("Scheduler is running...")  # Debugging print
        time.sleep(5)

# Start the scheduler in a separate thread

def start_scheduler():
    global scheduler_running
    if not scheduler_running:
        scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
        scheduler_thread.start()
        return "Scheduler started!"
    return "Scheduler is already running."

# Add job to schedule
schedule.every(10).seconds.do(job)