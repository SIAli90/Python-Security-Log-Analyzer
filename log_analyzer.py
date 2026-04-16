from collections import defaultdict

# Store failed login attempts per IP
failed_attempts = defaultdict(int)

# Store successful logins
success_logins = set()

# Suspicious threshold
THRESHOLD = 3

with open("auth.log", "r") as file:
    for line in file:
        parts = line.split()
        ip = parts[-1].split("=")[1]

        if "LOGIN_FAILED" in line:
            failed_attempts[ip] += 1

        elif "LOGIN_SUCCESS" in line:
            success_logins.add(ip)

print("\n=== Suspicious Activity Report ===\n")

for ip, count in failed_attempts.items():
    print(f"{ip} -> {count} failed attempts")

print("\n=== Potential Brute Force IPs ===\n")

for ip, count in failed_attempts.items():
    if count >= THRESHOLD:
        print(f"[ALERT] {ip} exceeded threshold with {count} failed logins")

print("\n=== Suspicious Success After Failures ===\n")

for ip in success_logins:
    if failed_attempts[ip] > 0:
        print(f"[WARNING] {ip} had failed attempts before success")