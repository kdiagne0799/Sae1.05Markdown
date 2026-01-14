# 🛡️ NetTrace Investigator

![Python](https://img.shields.io/badge/Language-Python_3.x-blue?style=for-the-badge&logo=python)  
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)  
![Domain](https://img.shields.io/badge/Domain-Network_Threat_Analysis-red?style=for-the-badge)

---

## 📋 Contexte pédagogique

Ce projet a été réalisé dans le cadre de la **SAE 1.05 - Traiter des données** (BUT Réseaux & Télécommunications - Semestre 1) à l'IUT de Roanne.

**Problématique :** Le réseau d'une entreprise sature. Parviendrez-vous à identifier pourquoi ?

### 🎯 Compétences visées

**Compétence RT3** : Créer des outils et applications informatiques pour les Réseaux & Télécommunications

**Apprentissages critiques mobilisés :**
- **AC03.11** : Utiliser un système informatique et ses outils
- **AC03.12** : Lire, exécuter, corriger et modifier un programme
- **AC03.13** : Traduire un algorithme dans un langage et pour un environnement donné
- **AC03.14** : Connaître l'architecture et les technologies d'un site Web
- **AC03.15** : Choisir les mécanismes de gestion de données adaptés au développement de l'outil
- **AC03.16** : S'intégrer dans un environnement propice au développement et au travail collaboratif

### 📦 Livrables

- ✅ Code Python hébergé sur GitHub
- ✅ Notice d'utilisation en anglais (README)
- ✅ Présentation orale de 12 minutes avec démonstration
- ✅ Portfolio avec pièces justificatives

---

## 📖 Overview

**NetTrace Investigator** is a small Python toolchain designed to analyze raw network traces (exported from `tcpdump`) and produce a structured security report (Markdown → HTML). 

The goal is to transform hard-to-read raw dumps into clear, actionable outputs highlighting suspicious behaviors and relevant indicators, helping network administrators identify security threats such as SSH brute force attacks, port scans, and SYN floods.

This project was developed to investigate network saturation issues in a production environment by processing `tcpdump` logs when traditional analysis methods (Wireshark, configuration checks) failed to identify the root cause.

---

## ⚙️ Key Features

### 📊 **Data preparation**
- Read a dump file (`DumpFile.txt` from `tcpdump` command).
- Extract relevant fields: IP addresses, ports, timestamps, TCP flags, protocols.
- Export clean structured data to CSV format (`Network_Analysis.csv`) for further analysis.

### 🔍 **Security analysis**
The tool detects common attack patterns using threshold-based heuristics:

- **SSH Brute Force Detection**
  - Threshold: More than **50 SSH connection attempts** (port 22) from a single source IP within a 5-minute window.
  - Logic: Groups SSH packets by source IP and timestamp, flags IPs exceeding the threshold.

- **Port Scan Detection**
  - Threshold: A single source IP connects to **more than 20 different destination ports** on the same target.
  - Logic: Analyzes unique (src_ip, dst_ip, dst_port) combinations to identify scanning behavior.

- **SYN Flood Detection (DoS)**
  - Threshold: More than **100 SYN packets** sent to a single destination IP within a short time frame.
  - Logic: Counts TCP SYN flags per destination, identifies abnormal SYN rates indicating potential denial-of-service attacks.

- **Unencrypted Traffic Detection**
  - Identifies traffic on risky unencrypted ports: HTTP (80), Telnet (23), FTP (21).
  - Recommends migration to secure alternatives (HTTPS, SSH, SFTP).

- **Top Talkers Analysis**
  - Lists most active IPs by packet count to identify bandwidth hogs or compromised hosts.
📝 PARTIE 2 - Milieu du README (lignes 81-160)
text
### 📄 **Reporting**
- Generate a detailed Markdown report (`Network_Report.md`) with:
  - Executive summary of findings
  - Detailed alerts with timestamps and IP addresses
  - Traffic statistics and top talkers
  - Recommendations for remediation
- Convert Markdown to styled HTML page (`Network_Report.html`) for easy sharing and presentation.

---

## 🔄 Pipeline

```mermaid
flowchart LR
    A[DumpFile.txt<br/>tcpdump raw output] --> B[txt_to_csv.py<br/>Extraction & Parsing]
    B --> C[Network_Analysis.csv<br/>Structured data]
    C --> D[csv_to_md.py<br/>Security Analysis]
    D --> E[Network_Report.md<br/>Markdown report]
    E --> F[md_to_html.py<br/>HTML Conversion]
    F --> G[Network_Report.html<br/>Final styled report]
    C --> H[Excel Analysis<br/>Charts & Pivot Tables]
📁 Project structure
File	Purpose
DumpFile.txt	Example raw dump from tcpdump command
txt_to_csv.py	Extraction, parsing, and cleanup → CSV output
csv_to_md.py	Security analysis → generate Markdown report
md_to_html.py	Convert Markdown report → styled HTML
Network_Analysis.csv	Structured data (Excel/Pandas ready)
Network_Report.md	Security analysis report (Markdown format)
Network_Report.html	Final styled report (HTML format)
README.md	User manual (English, this file)
🛠️ Requirements
Python 3.x (tested on Python 3.8+)

Standard library only — no external packages required

os, csv, re, collections, argparse, datetime

Optional: Excel for manual CSV analysis

🚀 Quick start
Run the full pipeline from the project root directory:

bash
# Step 1: Convert raw dump to CSV
python txt_to_csv.py
# → Generates Network_Analysis.csv

# Step 2: Analyze CSV and generate Markdown report
python csv_to_md.py
# → Generates Network_Report.md

# Step 3: Convert Markdown to HTML
python md_to_html.py
# → Generates Network_Report.html
Each script can be executed separately if you only need a specific step.

📖 Usage (detailed)
1️⃣ txt_to_csv.py - Extract data from raw dump
Input: DumpFile.txt (raw tcpdump output)
Output: Network_Analysis.csv (structured data)

bash
python txt_to_csv.py [--input DumpFile.txt] [--output Network_Analysis.csv]
What it does:

Parses each line of the tcpdump output

Extracts: timestamp, source IP, source port, destination IP, destination port, protocol, TCP flags

Cleans and normalizes data

Exports to CSV format with proper headers

text

***

## 📝 **PARTIE 3 - Fin du README (lignes 161-fin)**

```markdown
### 2️⃣ `csv_to_md.py` - Analyze and generate report

**Input:** `Network_Analysis.csv`  
**Output:** `Network_Report.md`

```bash
python csv_to_md.py [--input Network_Analysis.csv] [--output Network_Report.md]
What it does:

Loads CSV data

Applies security detection algorithms (SSH brute force, port scans, SYN floods)

Identifies unencrypted traffic and top talkers

Generates structured Markdown report with:

Executive summary

Critical alerts with detailed evidence

Traffic statistics

Remediation recommendations

3️⃣ md_to_html.py - Convert to HTML
Input: Network_Report.md
Output: Network_Report.html

bash
python md_to_html.py [--input Network_Report.md] [--output Network_Report.html]
What it does:

Converts Markdown to HTML with embedded CSS

Applies professional styling (headers, tables, code blocks)

Creates a standalone HTML file ready for sharing or presentation

📊 Output format & examples
CSV Structure
Expected CSV header:

text
timestamp,src_ip,src_port,dst_ip,dst_port,protocol,flags,info
Example row:

text
2025-01-10 14:23:45,192.168.1.100,52341,10.0.0.5,22,TCP,S,SSH connection attempt
Markdown Report Example
text
## 🚨 Critical Alerts

### SSH Brute Force Detected
- **Source IP:** 192.168.190.130
- **Attempts:** 66 connection attempts in 5 minutes
- **Target:** 10.0.0.5:22
- **Recommendation:** Block source IP and enable fail2ban

### Port Scan Detected
- **Source IP:** 172.16.0.50
- **Ports scanned:** 35 unique ports on target 10.0.0.10
- **Recommendation:** Investigate source host for compromise
HTML Report
The HTML output includes:

✅ Professional styling with headers and color-coded sections

✅ Tables for structured data

✅ Embedded CSS (no external dependencies)

✅ Ready for presentation or email sharing

📈 Excel Analysis
The generated Network_Analysis.csv can be imported into Excel for additional analysis:

Open Excel and import Network_Analysis.csv

Create pivot tables to analyze:

Traffic volume by IP address

Port usage distribution

Timeline of suspicious activity

Generate charts:

Top 10 source IPs by packet count

Protocol distribution (TCP vs UDP)

Hourly traffic patterns

🔧 Development & Contributing
Code Structure
Modular design: Each script handles one specific transformation

Standard library only: No external dependencies for easy deployment

CLI arguments: Flexible input/output paths using argparse

PEP8 compliant: Clean, readable Python code with docstrings

Testing
Add test fixtures under tests/ directory

Provide sample DumpFile.txt with known attack patterns

Verify detection accuracy against expected results

Contribution Guidelines
Fork the repository

Create a feature branch: git checkout -b feature/new-detection

Commit small, focused changes with clear messages

Submit a pull request with detailed description

Future Improvements
🔹 Add CLI filters for time ranges and specific IPs

🔹 Export results to JSON format for integration with SIEM tools

🔹 Implement machine learning for anomaly detection

🔹 Add real-time monitoring mode for live tcpdump feeds

🔹 Create web dashboard for interactive visualization

🎓 Learning Outcomes
This project demonstrates:

✅ AC03.11: Use of Python, Git, and command-line tools

✅ AC03.12: Reading, modifying, and debugging Python programs

✅ AC03.13: Translating security analysis logic into Python algorithms

✅ AC03.14: Understanding web technologies (Markdown → HTML conversion)

✅ AC03.15: Choosing appropriate data structures (CSV, dictionaries, lists)

✅ AC03.16: Using GitHub for collaborative development and version control

📜 License & Contact
License: This project is provided as-is for educational purposes (SAE 1.05). Add a LICENSE file if you wish to define specific open-source terms.

Author: Khadim Diagne

Contact: kdiagne799@gmail.com

GitHub: kdiagne0799/Sae1.05_Network_Report

🙏 Acknowledgments
IUT de Roanne - BUT Réseaux & Télécommunications

SAE 1.05 teaching team for providing the project framework

tcpdump maintainers for the network capture tool

Python community for excellent standard library documentation

