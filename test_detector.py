from soc_detector import extract_ip

# A normal failed-login line should give back the IP
line = "Oct 25 11:15:01 kampala-server sshd[1002]: Failed password for root from 45.33.32.156 port 22"
assert extract_ip(line) == "45.33.32.156"

# A line with no IP should give back None, not crash
assert extract_ip("garbage line with no ip") is None

# A line with "from" but no IP should also be safe
assert extract_ip("Failed password for from_admin port 22") is None

print("All tests passed")
