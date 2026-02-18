# Basic Keylogger Tool

## 📌 Objective
The primary goal of this project was to understand the mechanics of keystroke logging from a cybersecurity perspective. By developing this tool, I explored how malware interacts with operating system APIs to intercept user input and how to develop effective defensive countermeasures.

## 🏗️ Tech Stack
* **Language:** C / C++ (WinAPI)
* **Environment:** Windows OS
* **Analysis Tools:** Process Monitor, Wireshark (for behavioral mapping)

## ⚙️ Key Features
* **Keystroke Capture:** Implemented low-level hooks to intercept and record keyboard input in real-time.
* **Local Logging:** Securely stored captured data into hidden local files for analysis.
* **Execution Flow Mapping:** Analyzed the tool's behavior to understand how such utilities maintain persistence on a host system.

## 🛡️ Defensive Analysis & Countermeasures
As part of this project, I performed a behavioral analysis of the compiled executable to identify its footprint. I developed strategies for detection, including:
* **Host-Based Detection:** Identifying anomalous API calls related to keyboard hooking.
* **Process Monitoring:** Detecting unauthorized background processes with high CPU or I/O activity.

## ⚠️ Disclaimer
This project was created for educational and ethical security research purposes only. Unauthorized use of such tools is illegal.
