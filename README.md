# 🛢 Oil Rig Raspberry Pi Control System

A **Raspberry Pi-based dashboard** for monitoring and controlling oil rig sensors and systems using GPIO and WiFi. Built with **Flask**, **Tailwind CSS**, and modern web standards, this project provides real-time status, interactive controls, and user-friendly documentation.

**Live Demo:** [View the Dashboard](https://pason.cohogs.com)


<img width="1718" height="813" alt="Oil Rig Control Panel - Raspberry Pi" src="https://github.com/user-attachments/assets/530ce87a-f165-47a7-b36c-3379ee2ee559" />


---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [System Architecture](#system-architecture)  
4. [Hardware Requirements](#hardware-requirements)  
5. [Software Requirements](#software-requirements)  
6. [Setup and Installation](#setup-and-installation)  
7. [Usage](#usage)  
8. [Flask API Endpoints](#flask-api-endpoints)  
9. [Dashboard Sections](#dashboard-sections)  
10. [User Guide](#user-guide)  
11. [Safety Considerations](#safety-considerations)  
12. [Contributing](#contributing)  
13. [License](#license)  
14. [Contact](#contact)  

---

## Project Overview

This project allows real-time monitoring and control of oil rig sensors and equipment through a web-based dashboard. The system can:  

- Display **sensor readings** (pressure, temperature, gas levels)  
- Control **critical rig systems** (Blowout Preventer, Mud Pump, Emergency Alarm)  
- Show **active systems** in real-time  
- Provide a **user-friendly guide** for operators  
- Work in a **hybrid environment**, with some devices simulated for testing  

The project is built to be modular and easily extensible for additional sensors or control systems.

---

## Features

- **Interactive Dashboard**: Displays sensors and control buttons  
- **Active Systems Section**: Shows which devices are currently ON  
- **Confirmation Prompts**: Safety confirmations before toggling critical systems  
- **Dynamic Buttons**: “Activate/Deactivate” labels based on device state  
- **WiFi & Server Status Indicators**: Real-time connectivity feedback  
- **User Guide**: Embedded, accessible guide for operators  
- **Tailwind CSS**: Clean, responsive design  
- **Flask Backend**: Handles API requests and device state management  

---

## System Architecture
<img width="3364" height="2121" alt="Wiring Diagram" src="https://github.com/user-attachments/assets/a07e2e9d-9567-445b-ad53-c98a267e5f0b" />



**Flow:**  

1. Sensors report readings to the Flask app (or simulated values).  
2. Flask app serves HTML pages and APIs.  
3. Operators view live data, toggle devices, and see active systems.  
4. User guide provides operational instructions and emergency procedures.  

---

## Hardware Requirements

- Raspberry Pi 4 (or any Pi with GPIO)  
- Breadboard & jumper wires (for testing sensors)  
- GPIO sensors:  
  - Pressure sensor  
  - Temperature sensor  
  - Gas sensor  
- GPIO outputs for:  
  - Blowout Preventer actuator  
  - Mud Pump relay  
  - Emergency Alarm system  
- WiFi connectivity  

---

## Software Requirements

- Raspberry Pi OS (or Linux with Python 3.9+)  
- Python 3.9+  
- Flask (`pip install flask`)  
- Optional: GPIO library (e.g., `RPi.GPIO`) for real hardware control  
- Web browser for dashboard access  

---

## Setup and Installation

1. **Clone the Repository**  

```bash
git clone https://github.com/GeorgioChahoud/Oil-Rig-Raspberry-Pi-Control-System.git
cd Oil-Rig-Raspberry-Pi-Control-System
```

2. **Install Python Dependencies
```bash
pip install flask
```

3. **Directory Structure
```code
oilrig-pi-dashboard/
├─ app.py                 # Flask backend
├─ templates/
│  ├─ index.html          # Dashboard
│  └─ user-guide.html     # User guide
├─ static/
│  └─ css/                # Optional custom CSS
└─ README.md
```

4. **Run Flask App
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0
```

5. **Access Dashboard
 ```code
http://<raspberry_pi_ip>:5000/
```

## Flask API Endpoints

| Endpoint                  | Method | Description |
|----------------------------|--------|-------------|
| `/api/toggle/<device>`     | POST   | Toggle a device (`bop`, `pump`, `alarm`) |
| `/api/toggle-states`       | GET    | Return current ON/OFF state of all devices |
| `/api/status`              | GET    | Return WiFi and server connectivity status |

**Sample Response (`/api/toggle-states`)**  

```json
{
  "bop": true,
  "pump": false,
  "alarm": true
}
```

## Dashboard Sections

1. **Sensor Readings**: Displays real-time simulated or live sensor data.  
2. **Control Systems**: Buttons to toggle critical equipment, with safety confirmation dialogs.  
3. **Active Systems**: Shows all currently ON systems, with color-coded badges.  
4. **Status Indicators**: Displays WiFi and server connectivity using green/red dots.

## User Guide

Accessible via **User Guide** link in the header. Includes:  

- System Overview  
- Dashboard Overview  
- Safety Thresholds  
- Operating Instructions  
- Emergency Procedures  
- Contact Information

## Safety Considerations

- **Always confirm before toggling critical systems.**  
- **Emergency Alarm** should be activated only in actual emergencies.  
- **Mud Pump & BOP** toggling should follow operational protocols.  
- Simulation mode is safe for testing; real GPIO hardware requires caution.

## Contact

- **Project Lead**: Oil Rig Systems Team  
- **Support**: techsupport@pason.com
- **Emergency**: +1 (877) 255-3158
