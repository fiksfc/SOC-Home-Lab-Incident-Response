from collections import Counter
import subprocess
import sys
import re
#Return the IP after "from" or None if the line has no IP.
def extract_ip(line):
    m = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
    if m:
        return m.group(1)
    return None
    # Only run this part when run directly, not when imported for testing
if __name__ == "__main__":
    print("--- SOC Analysis ---")
    with open("auth.log") as f:
        lines = f.readlines()

    failed = []
    for line in lines:
        if "Failed password" in line:
            #find the ip after "from"
           ip = extract_ip(line)

    if ip:
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
