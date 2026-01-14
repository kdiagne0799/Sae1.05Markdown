# 🛡️ SAE1.05 Network Traffic Analysis Tool

## 📋 Prerequisites

### Required Python Version
- **Python 3.8 or higher**

### Required Libraries
```python
os              # File operations (included with Python)
csv             # CSV file handling (included with Python)
re              # Regular expressions (included with Python)
collections     # Data structures (included with Python)
datetime        # Timestamp handling (included with Python)
No external packages needed! Everything uses Python's standard library.

Optional Software
Microsoft Excel (for manual data analysis and pivot tables)

🎯 What This Project Does
This tool helps you find out why a network is having problems. It reads network traffic files (tcpdump format) and tells you if something suspicious is happening - like SSH brute force attacks, port scans, or ICMP floods.

I built this for my university project at IUT Roanne. The idea was simple: our company has two sites (one in France, one in India), and the network in India was having issues. Normal checks didn't work, so I created these Python programs to dig deeper into the traffic data.

📦 What's Inside
The project has three main Python scripts:

Script	Purpose
txt_to_csv.py	Converts raw tcpdump text file → clean CSV spreadsheet
csv_to_md.py	Analyzes CSV data → generates Markdown report with security alerts
md_to_html.py	Converts Markdown report → styled HTML page for presentation
Files Generated
Network_Analysis.csv - Structured data (semicolon-separated)

Network_Report.md - Security analysis report (Markdown format)

Network_Report.html - Final styled report (HTML with embedded CSS)

⚙️ How It Works
📝 txt_to_csv.py Explained
The first script reads your raw tcpdump output and extracts all the important information:

⏰ Timestamp - When each packet was sent

🔌 Protocol - TCP, UDP, ICMP, etc.

📍 Source IP & Port - Where it came from

🎯 Destination IP & Port - Where it was going

🚩 TCP Flags - SYN, ACK, FIN, RST, etc.

📏 Packet Length - Size of each packet

Then it saves everything into a CSV file with semicolon separators for easy Excel import.

Example Input (DumpFile.txt):

text
15:34:04.766656 IP 192.168.1.100.52341 > 10.0.0.5.22: Flags [S], seq 0, win 65535, length 0
Example Output (Network_Analysis.csv):

text
Timestamp;Source_IP;Source_Port;Dest_IP;Dest_Port;Protocol;Flags;Length;Packet_Info
15:34:04.766656;192.168.1.100;52341;10.0.0.5;22;TCP;S;60;SSH connection attempt
🔍 csv_to_md.py Explained
The second script reads your CSV file and does the detective work. It looks for three main security threats:

🚨 Detection Thresholds
Attack Type	Description	Threshold
🔴 SSH Brute Force	When one IP sends too many SSH connection attempts to port 22	> 50 SSH packets in 5 minutes
🟠 Port Scanning	When one IP is checking many different ports on your network	> 20 different destination ports
🟡 ICMP Flood (DoS)	When one IP sends excessive ICMP packets (ping flood)	> 50 ICMP packets
What Gets Detected in Your Network
Based on the actual analysis of DumpFileB2.txt, here's what was found:

🔴 1. Critical Threat: Targeted SSH Attack
Source IP: 192.168.190.130

Attack Type: SSH Brute Force (66 packets to port 22)

Severity: HIGH 🔴

Recommendation: Block source IP immediately, enable fail2ban

🟠 2. Port Scanning Activity
Scanned Ports: 135 different ports probed

Severity: MEDIUM ⚠️

Recommendation: Investigate source host for compromise

🟡 3. ICMP Flood Detected
Packets: 84 ICMP packets detected

Severity: MEDIUM ⚠️

Potential: Denial of Service (DoS) attempt

Recommendation: Rate-limit ICMP traffic

After analyzing, it creates:

✅ Network_Report.md - Detailed Markdown report with all statistics and alerts

✅ Lists of suspicious IPs with severity levels

✅ Top 10 most active IP addresses

✅ Protocol distribution statistics

🎨 md_to_html.py Explained
The third script converts your Markdown report into a professional HTML page with:

🎨 Embedded CSS styling (Bootstrap-inspired)

🟥🟧🟩 Color-coded alert sections (red = critical, orange = warning)

📊 Clean tables for data presentation

🌐 Standalone file (no external dependencies, easy to email or present)

📊 What You Get
When you run all three scripts, here's what gets created:

1. Network_Analysis.csv
All your network packets in a neat table format (semicolon-separated).

Columns:

text
Timestamp;Source_IP;Source_Port;Dest_IP;Dest_Port;Protocol;Flags;Length;Packet_Info
2. Network_Report.md
A text document with:

📈 Total packets analyzed: 11,016 packets

📦 Total data volume: Statistics per IP

🏆 Top 10 most active IPs

📡 Protocol distribution: TCP, UDP, ICMP percentages

🚨 Security alerts: 3 threats detected

Example Report Excerpt:

text
## 🚨 Critical Alerts

### 1. Critical Threat: Targeted SSH Attack
🔴 **Main Assault**: `192.168.190.130` (66 packets). Brute Force confirmed.

### 2. Other Detected Anomalies
⚠️ **Port Scanning**: Host probed **135** different ports.
⚠️ **ICMP Flood**: 84 packets detected. Potential DoS.
3. Network_Report.html
Professional styled HTML page ready for:

📧 Email sharing with your team

🎤 Presentation during your oral defense (12 min)

📁 Portfolio submission

🚀 How to Use This
Installation
No packages to install! Just make sure you have Python 3.8+.

Then clone the project:

bash
git clone https://github.com/kdiagne0799/Sae1.05_Network_Report.git
cd Sae1.05_Network_Report
🧗 Step-by-Step Usage
👍 Step 1: Convert your tcpdump file
Run the first script:

bash
python txt_to_csv.py
What happens:

text
Démarrage de la conversion...
Lecture : DumpFileB2.txt
Lignes lues : 507,891
Paquets extraits : 11,016
Lignes ignorées : 496,875
Fichier créé : Network_Analysis.csv
The program reads your DumpFileB2.txt file and creates Network_Analysis.csv with all packets in structured format.

👍 Step 2: Analyze the data
Run the second script:

bash
python csv_to_md.py
What happens:

text
========== ANALYSE DEMARREE ==========

Lecture de Network_Analysis.csv...
11,016 paquets lus
Analyse en cours...
Détection des anomalies...

🚨 ALERTES DETECTEES :
  - SSH Brute Force : 192.168.190.130 (66 packets)
  - Port Scan : 135 ports probed
  - ICMP Flood : 84 packets

Rapport créé : Network_Report.md

========== ANALYSE TERMINEE ==========
👍 Step 3: Generate HTML report
Run the third script:

bash
python md_to_html.py
What happens:

text
Conversion Markdown → HTML...
Lecture : Network_Report.md
Génération HTML avec CSS...
Fichier créé : Network_Report.html

✅ Rapport HTML prêt pour présentation !
👍 Step 4: Check the results
You'll now have these files:

text
Sae1.05_Network_Report/
├── DumpFileB2.txt            # Your original tcpdump file
├── Network_Analysis.csv      # Structured data (Excel-ready)
├── Network_Report.md         # 📄 Read this first! Main report
├── Network_Report.html       # 🌐 Professional styled version
├── txt_to_csv.py            # Script 1
├── csv_to_md.py             # Script 2
├── md_to_html.py            # Script 3
└── README.md                # This file
What to read:

Network_Report.md - Read this first. It tells you everything.

Network_Report.html - Open in browser for styled version.

If there are problems, they'll be clearly listed with 🔴 red or 🟠 orange warnings.

🔍 Understanding the Results
✅ If No Problems Found
The report will say:

text
