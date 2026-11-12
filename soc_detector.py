from collections import Counter
import subprocess
import sys

print("--- SOC Analysis ---")
with open("auth.log") as f:
    lines = f.readlines()

failed = []
for line in lines:
    if "Failed password" in line:
        ip = line.split("from")[1].split()[0]
        failed.append(ip)

count = Counter(failed)
for ip, c in count.items():
    print(f"IP {ip} failed {c} times")
    if c > 5:
    
        print(f"🚨 ALERT! Brute-Force Detected from {ip}!")
        print(f"Recommendation: BLOCK IP {ip} immediately")
        subprocess.run([sys.executable, "soc_responder.py", ip])
        print("Evidence:")
        for l in lines:
            if ip in l and "Failed" in l:
                print(f" - {l.strip()}")
