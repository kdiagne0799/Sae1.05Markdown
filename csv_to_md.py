import csv
import os
from collections import Counter

# Se placer dans le dossier du script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def interpret_flags(flag_val, packet_info):
    """Interprétation basée sur la colonne Flags."""
    f = flag_val.upper()
    if "S" in f: return "Connection Request (SYN)"
    if "P" in f: return "Data Transfer (PUSH)"
    if "R" in f: return "Connection Refused (RST)"
    if "." in f: return "Acknowledgment (ACK)"
    if "ICMP" in packet_info.upper(): return "Ping/Network Diagnostic"
    return "Other"

def generate_final_report(input_csv, output_md):
    try:
        if not os.path.exists(input_csv):
            print(f"Error: {input_csv} not found.")
            return

        with open(input_csv, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter=';')
            packets = list(reader)

        if not packets:
            print("Error: The CSV file is empty.")
            return

        # --- 1. ANALYSE (Basée sur vos nouvelles colonnes) ---
        
        # SSH : On regarde si Dest_Port est 22 ou ssh
        ssh_packets = [p for p in packets if p['Dest_Port'] in ['22', 'ssh']]
        ssh_counts = Counter([p['Source_IP'] for p in ssh_packets])
        
        # Scan de Port : On compte les ports uniques (Dest_Port)
        dest_ports = [p['Dest_Port'] for p in packets]
        unique_dest_ports = len(set(dest_ports))

        # ICMP : On regarde Packet_Info
        icmp_packets = [p for p in packets if "ICMP" in p['Packet_Info']]

        # Telnet : On regarde si Dest_Port est 23 ou telnet
        telnet_attempts = [p for p in packets if p['Dest_Port'] in ['23', 'telnet']]

        # --- 2. GÉNÉRATION DU RAPPORT MARKDOWN ---
        with open(output_md, 'w', encoding='utf-8') as md:
            md.write("# 🛡️ Global Network Security Report\n\n")
            
            # --- Section Menaces ---
            md.write("## 1. Critical Threat: Targeted SSH Attack\n")
            if not ssh_counts:
                md.write("- ✅ No specific SSH threats detected.\n")
            else:
                for source, count in ssh_counts.items():
                    if count >= 40:
                        md.write(f"- 🔴 **Main Assault**: `{source}` ({count} packets). Brute Force confirmed.\n")
                    else:
                        md.write(f"- 🟡 **Stealth Probe**: `{source}` ({count} packets). Potential reconnaissance.\n")

            md.write("\n## 2. Other Detected Anomalies\n")
            
            if unique_dest_ports > 5:
                md.write(f"- ⚠️ **Port Scanning**: Host probed **{unique_dest_ports}** different ports.\n")
            
            if len(icmp_packets) > 20:
                md.write(f"- ⚠️ **ICMP Flood**: {len(icmp_packets)} packets detected. Potential DoS.\n")

            if telnet_attempts:
                md.write(f"- ❌ **Insecure Protocol**: {len(telnet_attempts)} Telnet attempts detected (Port 23).\n")

            # --- Section Tableau (Avec TOUTES vos colonnes) ---
            md.write("\n## 3. Traffic Sample (Top 30)\n")
            
            # En-tête du tableau Markdown correspondant à vos colonnes
            md.write("| Timestamp | Source IP | Src Port | Dest IP | Dest Port | Flags | Length | Info |\n")
            md.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
            
            for p in packets[:30]:
                # Extraction sécurisée des données
                ts = p.get('Timestamp', '')
                sip = p.get('Source_IP', '')
                sport = p.get('Source_Port', '')
                dip = p.get('Dest_IP', '')
                dport = p.get('Dest_Port', '')
                flg = p.get('Flags', '')
                lng = p.get('Length', '')
                nfo = p.get('Packet_Info', '')[:30] + "..." # On coupe un peu si c'est trop long
                
                # Écriture de la ligne
                md.write(f"| {ts} | {sip} | {sport} | {dip} | {dport} | `{flg}` | {lng} | {nfo} |\n")

        print(f"Success! Report generated: {output_md}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generate_final_report('Network_Analysis.csv', 'Network_Report.md')