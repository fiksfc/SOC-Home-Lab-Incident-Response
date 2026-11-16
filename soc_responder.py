import datetime
import sys

if len(sys.argv) < 2:
    attacker_ip = input("Enter the IP address to block: ")
else:
    attacker_ip = sys.argv[1]
    #insteady of giving an error be a gentalman and just ask for the ip to block
try:
    with open("blocked_ips.txt", "r") as f:
        if attacker_ip in f.read():
            print(f"[INFO] {attacker_ip} already blocked. Skipping.")
            exit()
except FileNotFoundError:    pass
 #this line ^ checks if blocked already before adding

print(f"[{datetime.datetime.now()}] Starting auto-response...")
print(f"Blocking IP {attacker_ip}...")

with open("blocked_ips.txt", "a") as f:
    f.write(f"{attacker_ip} - blocked on {datetime.datetime.now()}\n")

print(f"[SUCCESS] {attacker_ip} has been blocked and added to blocked_ips.txt")
print(f"Sending email alert to SOC team: fikstella@soc.com")
#simulated:no realemail is sent
#its just a study enviroment
