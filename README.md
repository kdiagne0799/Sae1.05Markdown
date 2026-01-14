# 🛡️ SAE1.05 Network Traffic Analysis Tool

## 📋 Prerequisites

### Required Python Version

- **Python 3.8 or higher**

### Required Libraries

All required modules are included in the Python standard library:

```python
os              # File operations
csv             # CSV file handling
re              # Regular expressions
collections     # Data structures (Counter, defaultdict)
datetime        # Timestamp handling
```

No external packages needed.

**Optional software:** Microsoft Excel (for manual data analysis and pivot tables)

---

## 🎯 What this project does

This tool helps you find out why a network is having problems. It reads network traffic files (tcpdump format) and detects suspicious activities such as SSH brute force attacks, port scans, and ICMP floods.

This project was developed for a university assignment at IUT Roanne: two company sites (France and India) experienced network issues and needed deeper traffic analysis than standard tools provided.

---

## 📦 What's inside

### Scripts and purpose

| Script | Purpose |
|---|---|
| `txt_to_csv.py` | Converts raw tcpdump text file → clean CSV (semicolon-separated) |
| `csv_to_md.py` | Analyzes CSV → generates Markdown report with security alerts |
| `md_to_html.py` | Converts Markdown report → styled HTML page for presentation |

### Files generated

- `Network_Analysis.csv` — Structured data (semicolon-separated)
- `Network_Report.md` — Security analysis report (Markdown)
- `Network_Report.html` — Final styled report (HTML with embedded CSS)

---

## ⚙️ How it works

### txt_to_csv.py — parsing raw tcpdump

The script extracts:

- Timestamp — when each packet was captured
- Protocol — TCP, UDP, ICMP, etc.
- Source IP & Port
- Destination IP & Port
- TCP Flags — SYN, ACK, FIN, RST, etc.
- Packet Length

It writes a CSV with semicolon separators so it can be easily opened in Excel.

**Example input (excerpt from DumpFile.txt):**

```
15:34:04.766656 IP 192.168.1.100.52341 > 10.0.0.5.22: Flags [S], seq 0, win 65535, length 0
```

**Example output (CSV row):**

```
Timestamp;Source_IP;Source_Port;Dest_IP;Dest_Port;Protocol;Flags;Length;Packet_Info
15:34:04.766656;192.168.1.100;52341;10.0.0.5;22;TCP;S;60;SSH connection attempt
```

### csv_to_md.py — detection & reporting

The script applies simple heuristic thresholds to identify suspicious patterns.

#### Detection thresholds

| Attack type | Description | Threshold |
|---|---:|---:|
| SSH brute force | Many SSH attempts (port 22) from one IP | > 50 SSH packets in 5 minutes |
| Port scanning | One IP probes many distinct destination ports | > 20 different destination ports |
| ICMP flood (DoS) | Excessive ICMP packets from one IP | > 50 ICMP packets |

#### Example detections (from DumpFileB2.txt analysis)

- 🔴 Critical: Targeted SSH attack — Source: `192.168.190.130` (66 SSH packets to port 22)
  - Severity: HIGH
  - Recommendation: block the IP, enable fail2ban

- 🟠 Port scanning — 135 ports probed
  - Severity: MEDIUM
  - Recommendation: investigate the source host

- 🟡 ICMP flood — 84 ICMP packets detected
  - Severity: MEDIUM
  - Recommendation: rate-limit ICMP or apply filtering

The script produces `Network_Report.md` with:

- Executive summary
- Lists of suspicious IPs and severity
- Top 10 active IPs and protocol distribution
- Recommendations

### md_to_html.py — presentation

Converts `Network_Report.md` to a standalone `Network_Report.html` with:

- Embedded CSS (Bootstrap-inspired styles)
- Color-coded alerts (red/orange/green)
- Tables and sections ready for presentation or emailing

---

## 📊 What you get

### 1) `Network_Analysis.csv`

CSV table with columns:

```
Timestamp;Source_IP;Source_Port;Dest_IP;Dest_Port;Protocol;Flags;Length;Packet_Info
```

### 2) `Network_Report.md`

Includes:

- Total packets analyzed (e.g., 11,016)
- Total data volume statistics
- Top 10 most active IPs
- Protocol distribution: TCP, UDP, ICMP
- Security alerts (e.g., 3 threats detected)

**Example report excerpt:**

```markdown
## 🚨 Critical Alerts

### 1. Critical Threat: Targeted SSH Attack
🔴 **Main Assault**: `192.168.190.130` (66 packets). Brute Force confirmed.

### 2. Other Detected Anomalies
⚠️ **Port Scanning**: Host probed **135** different ports.
⚠️ **ICMP Flood**: 84 packets detected. Potential DoS.
```

### 3) `Network_Report.html`

A styled HTML page suitable for:

- Email sharing
- Presentation during the oral defense
- Portfolio submission

---

## 🚀 How to use

### Installation

No external packages required. Make sure Python 3.8+ is installed.

```bash
git clone https://github.com/kdiagne0799/Sae1.05_Network_Report.git
cd Sae1.05_Network_Report
```

### Step-by-step usage

1. Convert tcpdump file to CSV:

```bash
python txt_to_csv.py
```

Sample console output:

```
Démarrage de la conversion...
Lecture : DumpFileB2.txt
Lignes lues : 507,891
Paquets extraits : 11,016
Lignes ignorées : 496,875
Fichier créé : Network_Analysis.csv
```

1. Analyze the CSV and create markdown report:

```bash
python csv_to_md.py
```

Sample console output:

```
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
```

1. Generate an HTML report:

```bash
python md_to_html.py
```

Sample console output:

```
Conversion Markdown → HTML...
Lecture : Network_Report.md
Génération HTML avec CSS...
Fichier créé : Network_Report.html

✅ Rapport HTML prêt pour présentation !
```

### Files created

```
Sae1.05_Network_Report/
├── DumpFileB2.txt            # Your original tcpdump file
├── Network_Analysis.csv      # Structured data (Excel-ready)
├── Network_Report.md         # 📄 Read this first! Main report
├── Network_Report.html       # 🌐 Professional styled version
├── txt_to_csv.py             # Script 1
├── csv_to_md.py              # Script 2
├── md_to_html.py             # Script 3
└── README.md                 # This file
```

---

## 🔍 Understanding the results

If no problems are found, the report will indicate so and provide summary statistics. Otherwise, the report lists alerts with severity and suggested mitigations.

---

## 🧪 Tests & fixtures

Include a `/fixtures` folder with:

- `DumpFileB2_sample.txt` (trimmed sample dump)
- `Network_Analysis_sample.csv` (precomputed CSV)
- `Network_Report_sample.md` (expected report)

Recommended tests:

- Unit tests for `split_ip_port()` and timestamp extraction
- Integration test that runs the full pipeline against the sample dump and compares outputs

---

## 🔧 Development & Contributing

- Modular design: each script performs one transformation
- Standard library only for easy grading and reproducibility

Contribution guidelines:

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/name`
3. Add tests and documentation
4. Open a Pull Request with a clear description

---

## 🔮 Future improvements

- Add CLI arguments for time ranges and filters
- Export results to JSON for integration with SIEM tools
- Implement machine learning for anomaly detection
- Add real-time monitoring mode and web dashboard

---

## 🎓 Learning outcomes

This project demonstrates the following competencies (SAE 1.05):

- AC03.11 — Use of Python, Git, and command-line tools
- AC03.12 — Reading, modifying, and debugging Python programs
- AC03.13 — Translating security analysis logic into algorithms
- AC03.14 — Understanding web technologies (Markdown → HTML)
- AC03.15 — Choosing appropriate data structures (CSV, dicts, lists)
- AC03.16 — Using GitHub for collaborative development

---

## 📜 License & Contact

License: MIT (recommended)

Author: Khadim Diagne — contact: <kdiagne799@gmail.com>

---

If you want, I can also:

- add `fixtures/` and sample outputs ✅
- add `tests/` and basic unit/integration tests 🔧
- implement `run_report.py` to run the pipeline in one command ⚙️
