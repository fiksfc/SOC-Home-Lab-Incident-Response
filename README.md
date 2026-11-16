# SOC Home Lab - Incident Response

*Analyst:* Fikstella - SOC Tier 1 | Kampala, UG

*Lab Environment:* Linux (Debian) on Chromebook

### 🎯 Objective
Simulate a real SOC workflow: detect an SSH brute-force attack and automatically respond by blocking the attacker's IP.

### 📁 Tools Built
1. *soc_log_generator.py* - Generates 100 auth log lines with an attacker IP that fails more often than the others
2. *soc_detector.py* - Parses the logs, counts failed logins per IP, and raises an ALERT when an IP fails more than 5 times
3. *soc_responder.py* - Blocks the attacker IP and saves it to blocked_ips.txt. IPs that are already blocked are skipped. The email alert is simulated (a printed message)
4. *test_detector.py* - Tests that IP extraction works and that bad log lines are skipped without crashing

### 🚨 Attack Scenario Detected
- Attacker IP: 45.33.32.156
- Target users: root, admin, test, fik
- Pattern: repeated failed password attempts from one IP
- Action: ALERT + BLOCK

### ▶️ How to Run
bash
python3 soc_log_generator.py
python3 soc_detector.py
python3 test_detector.py

The detector runs the responder automatically when it finds an attacker, so you don't need to run it yourself.

### 🔧 Improvements After Mentor Review
- Connected the detector to the responder, so the flagged IP is passed in automatically
- Added a regex-based extract_ip function that safely skips lines with no IP
- Stopped duplicate entries in blocked_ips.txt
- Fixed invalid timestamps in the generated logs
- Added a test for the IP extraction

### 👩🏾‍💻 About This Project
I'm teaching myself cybersecurity. A month ago I didn't know how to start a computer/ Chromebook. Now I build, test and debug my own tools, and I'm improving them with feedback from my mentor.
