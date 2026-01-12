import csv
import re
import os

# Set working directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def split_ip_port(address):
    """Sépare l'adresse IP du port (ex: 192.168.1.1.80 -> 192.168.1.1, 80)."""
    parts = address.rsplit('.', 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    return address, "N/A"

def generate_clean_csv():
    """Reads DumpFile.txt and extracts detailed IP traffic into a CSV file."""
    try:
        with open('DumpFile.txt', 'r') as f:
            lines = f.readlines()

        with open('Network_Analysis.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            # Header row
            writer.writerow(['Timestamp', 'Source_IP', 'Source_Port', 'Dest_IP', 'Dest_Port', 'Flags', 'Length', 'Packet_Info'])

            for line in lines:
                if "IP" in line:
                    elements = line.split()
                    if len(elements) < 5: continue 

                    # --- MODIFICATION ICI : Extraction précise du Timestamp ---
                    # On cherche un motif type "Heures:Minutes:Secondes.Microsecondes"
                    # \d+ signifie "un ou plusieurs chiffres"
                    time_match = re.search(r'^(\d{2}:\d{2}:\d{2}\.\d+)', line.strip())
                    
                    if time_match:
                        timestamp = time_match.group(1) # Capture ex: 15:34:04.766656
                    else:
                        timestamp = elements[0] # Fallback si pas de microsecondes trouvées
                    
                    # Séparation IP et Port
                    src_ip, src_port = split_ip_port(elements[2])
                    dst_ip, dst_port = split_ip_port(elements[4].rstrip(':'))

                    # Extraction des Flags
                    flags_match = re.search(r'Flags \[(.*?)\]', line)
                    flags = flags_match.group(1) if flags_match else "None"

                    # Extraction de la taille (length)
                    length_match = re.search(r'length (\d+)', line)
                    length = length_match.group(1) if length_match else "0"

                    # Détails restants
                    packet_details = " ".join(elements[5:])
                    
                    writer.writerow([timestamp, src_ip, src_port, dst_ip, dst_port, flags, length, packet_details])
        
        print("Success: Network_Analysis.csv file created!")
    
    except FileNotFoundError:
        print("Error: DumpFile.txt not found. Please check the file path.")

if __name__ == "__main__":
    generate_clean_csv()