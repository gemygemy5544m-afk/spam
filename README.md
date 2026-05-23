
<h3 align="center">🚀 AF Tool — Advanced SMS Testing Utility for Termux on Android</h3>

<p align="center">
  Designed for <b>Security Researchers</b>, <b>Educators</b>, and <b>Ethical Hackers</b>.<br>
  Secure • Fast • Reliable • Anonymous
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AF-Tool-red?style=for-the-badge&logo=android&logoColor=white" alt="AF Tool"/>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/Termux-Compatible-green?style=for-the-badge&logo=linux" alt="Termux"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/badge/Status-Stable-success?style=for-the-badge" alt="Status"/>
  <img src="https://img.shields.io/badge/Contributions-Welcome-orange?style=for-the-badge&logo=github" alt="Contributions"/>
</p>

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Security Features](#-security-features)
- [Technical Details](#-technical-details)
- [Legal Disclaimer](#%EF%B8%8F-legal-disclaimer)
- [Developer](#-developer)
- [FAQ](#-af-tool-faq)
- [License](#-license)
- [Support](#-support-the-project)

---

## 🔍 Overview
**AF Tool** is a powerful **command-line SMS testing utility** developed to help security researchers and penetration testers simulate controlled SMS delivery tests securely and effectively.  
Its **core purpose** is to improve **cybersecurity awareness** and **network resilience** by providing a controlled testing environment.

---

## ✨ Features

| Feature             | Description                                              |
|--------------------|----------------------------------------------------------|
| 🔐 Secure Login     | Password-protected access with 3-attempt lockout        |
| 🌐 Proxy Rotation   | 15+ automatic rotating proxies for anonymity & reliability |
| 📞 Number Validation| Advanced phone number & country code verification       |
| 🎨 Interactive UI   | Modern terminal dashboard with colored progress bars   |
| 📊 Live Monitoring  | Real-time tracking of sent, failed, and pending SMS    |
| ⚡ Optimized APIs    | Private high-performance endpoints for better delivery rates |
| 🛡️ Privacy First     | Zero logs, no tracking, fully anonymous               |
| 📱 Termux Ready      | Optimized exclusively for Android + Termux            |

---

## 📋 Requirements

| Component  | Minimum Requirement          |
|------------|------------------------------|
| OS         | Android 7.0+                 |
| App        | [Termux](https://f-droid.org/en/packages/com.termux/)                       |
| Python     | 3.x or higher                |
| Storage    | Minimum 100MB free           |
| Internet   | Stable connection required   |

---

## 🚀 Installation

```bash
# Update Termux packages
pkg update && pkg upgrade -y

# Install dependencies
pkg install git python -y

# Clone the repository
git clone https://github.com/afroto/af-tool.git

# Enter project directory
cd af-tool

# Make installer executable
chmod +x afroto.sh

# Run installer
./afroto.sh
