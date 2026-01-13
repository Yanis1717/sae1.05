# Network Traffic Analysis Tool

![Python](https://img.shields.io/badge/Language-Python_3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Network_Forensics-red?style=for-the-badge)

## Overview
This project provides a set of scripts and tools to analyze, process, and report on network traffic data. It is designed to help users detect anomalies, security threats, and gain insights from raw network packet captures.

## What This Project Does
- Converts raw network dump files into structured CSV format for analysis.
- Analyzes network traffic to detect suspicious activities (e.g., SSH brute force, port scanning, ICMP floods).
- Generates human-readable reports in Markdown and HTML formats.
- Provides sample data and results for demonstration and testing.

## Architecture

## ⚙️ Architecture

The pipeline follows a strict modular approach:

```mermaid
graph LR
    A[DumpFile.txt] -->|txt_to_csv.py| B(Network_Analysis.csv)
    B -->|csv_to_md.py| C(Network_Report.md)
    C -->|md_to_html.py| D[Network_Report.html]
```

- **txt_to_csv.py**: Parses raw text dump files and converts them into a structured CSV file (`Network_Analysis.csv`).
- **csv_to_md.py**: Analyzes the CSV data, detects anomalies, and generates a Markdown report (`Network_Report.md`).
- **md_to_html.py**: Converts the Markdown report into an HTML file (`Network_Report.html`) for easy sharing and visualization.

## What's Inside
- `DumpFile.txt`: Example of a raw network dump file.
- `Network_Analysis.csv`: Structured CSV file generated from the dump.
- `Network_Report.md`: Markdown report with analysis results.
- `Network_Report.html`: HTML version of the report.
- `csv_to_md.py`, `txt_to_csv.py`, `md_to_html.py`: Main scripts for processing and analysis.
- `README.md`: Project documentation.

## Prerequisites
- Python 3.x
- No external libraries required (uses only Python standard library)

## How It Works
1. **Convert Dump to CSV**: Run `txt_to_csv.py` to process `DumpFile.txt` and generate `Network_Analysis.csv`.
2. **Analyze CSV**: Run `csv_to_md.py` to analyze the CSV and create a Markdown report (`Network_Report.md`).
3. **Generate HTML Report**: Run `md_to_html.py` to convert the Markdown report into HTML (`Network_Report.html`).

## Analysis Results (Sample Data)
Example findings from the sample data:
- **Critical Threat**: Targeted SSH brute force attack detected from IP `192.168.190.130` (66 packets).
- **Port Scanning**: Host probed 135 different ports.
- **ICMP Flood**: 84 packets detected, indicating a potential DoS attempt.

Sample traffic (see `Network_Report.md` for full details):
| Timestamp | Source IP | Src Port | Dest IP | Dest Port | Flags | Length | Info |
|-----------|-----------|----------|---------|-----------|-------|--------|------|
| 15:34:04.766656 | BP-Linux8 | ssh | 192.168.190.130 | 50019 | P. | 108 | Flags [P.], seq 2243505564:224... |
| 15:34:04.785366 | 192.168.190.130 | 50019 | BP-Linux8 | ssh | . | 0 | Flags [.], ack 108, win 7319, ... |

## Author
- Yanis L. 
BUT R&T student
