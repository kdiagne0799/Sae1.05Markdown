# 🛡️ NetTrace Investigator

![Python](https://img.shields.io/badge/Language-Python_3.x-blue?style=for-the-badge&logo=python)  
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)  
![Domain](https://img.shields.io/badge/Domain-Network_Threat_Analysis-red?style=for-the-badge)

## 📖 Vue d’ensemble

**NetTrace Investigator** est une petite chaîne d’outils pour analyser des traces réseau (export `tcpdump`) et produire un rapport structuré (Markdown → HTML). L’objectif est de transformer un fichier brut difficile à lire en un rapport qui met en avant comportements suspects et indicateurs pertinents pour la sécurité.

---

## 🚀 Fonctions principales

- **Préparation des données**
  - Lecture d’un fichier de dump (`DumpFile.txt`).
  - Extraction des champs (IP, ports, horodatage, indicateurs TCP).
  - Conversion en CSV exploitable (`Network_Analysis.csv`).

- **Analyse sécurité**
  - Détection de schémas d’attaque (brute force SSH, scans de ports, afflux de SYN).
  - Identification de flux non chiffrés (services à risque).

- **Restitution**
  - Génération d’un rapport Markdown (`Network_Report.md`).
  - Conversion du rapport en page HTML (`Network_Report.html`) pour présentation/archivage.

---

## ⚙️ Chaîne de traitement

```mermaid
graph LR
    A[DumpFile.txt] -->|txt_to_csv.py| B[Network_Analysis.csv]
    B -->|csv_to_md.py| C[Network_Report.md]
    C -->|md_to_html.py| D[Network_Report.html]
```

> Approche modulaire : chaque étape peut être modifiée indépendamment (ex. remplacer la génération HTML).

---

## 📦 Structure du projet

| Fichier | Rôle |
|---|---|
| `DumpFile.txt` | Exemple de journal brut exporté depuis tcpdump |
| `txt_to_csv.py` | Extraction/Nettoyage → CSV |
| `csv_to_md.py` | Analyse et génération du rapport en Markdown |
| `md_to_html.py` | Conversion Markdown → HTML |
| `Network_Analysis.csv` | Données structurées prêtes pour Excel/Pandas |
| `Network_Report.md` | Rapport d’analyse (Markdown) |
| `Network_Report.html` | Rapport final en HTML |

---

## 🧩 Prérequis

- Python 3.x  
- Bibliothèques standard uniquement (aucun paquet externe requis : `os`, `csv`, `re`, `collections`, ...)

---

## 🛠️ Utilisation

Exécuter la chaîne complète depuis le répertoire du projet :

1) Préparer les données :

```bash
python txt_to_csv.py
# Produit : Network_Analysis.csv
```

1) Analyser le trafic et générer le rapport Markdown :

```bash
python csv_to_md.py
# Produit : Network_Report.md
```

1) Produire le rapport HTML :

```bash
python md_to_html.py
# Produit : Network_Report.html
```

Chaque script peut être exécuté séparément si besoin.

---

## 🔍 Exemple de résultats

- IP tentant des connexions répétées sur SSH → suspicion de brute force.
- Volume anormal de SYN vers une même cible → possible début de DoS.

Les événements sont listés dans le rapport final avec IP/ports et résumés pour une lecture pédagogique.

---

## � Sommaire

- [Vue d’ensemble](#vue-densemble)
- [Fonctions principales](#fonctions-principales)
- [Quick start](#quick-start)
- [Utilisation détaillée](#utilisation-détaillée)
- [Format de sortie et exemples](#format-de-sortie-et-exemples)
- [Structure du projet](#structure-du-projet)
- [Développement & Contribuer](#développement--contribuer)
- [Licence & contact](#licence--contact)

---

## 🛠️ Utilisation détaillée

- `txt_to_csv.py`
  - Entrée : `DumpFile.txt`
  - Sortie : `Network_Analysis.csv`
  - Usage : `python txt_to_csv.py [--input DumpFile.txt] [--output Network_Analysis.csv]`

- `csv_to_md.py`
  - Entrée : `Network_Analysis.csv`
  - Sortie : `Network_Report.md`
  - Usage : `python csv_to_md.py [--input Network_Analysis.csv] [--output Network_Report.md]`

- `md_to_html.py`
  - Entrée : `Network_Report.md`
  - Sortie : `Network_Report.html`
  - Usage : `python md_to_html.py [--input Network_Report.md] [--output Network_Report.html]`



---

## 🔍 Format de sortie et exemples

- CSV attendu (exemple d’en-tête) :

```
timestamp,src_ip,src_port,dst_ip,dst_port,protocol,flags,info
```

- Exemples d’alertes générées dans le rapport :
  - IP 192.168.190.130 : 66 essais SSH en 5 min → suspicion brute force.
  - pic de SYNs → suspicion DoS.
