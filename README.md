# 🎮 VGC Guardian

> 🛡️ A friendly Windows GUI tool to **monitor** and **auto-restart** the **VGC service** (Riot Vanguard)  
> Perfect for Valorant players tired of unexpected Vanguard crashes stopping the game! 🚀

---

![Windows](https://img.shields.io/badge/Platform-Windows-blue.svg) ![Python](https://img.shields.io/badge/Python-3.6%2B-green.svg) ![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

https://youtu.be/CLLMTc7hQCA


## 🚀 Features

- 👀 Continuously monitors if the VGC service is running  
- 🔄 Automatically restarts the service if it crashes or stops  
- 🖥️ Clean, themed GUI with multiple stylish themes (Valorant, LoL Classic, Arcane, and more!)  
- 🛠️ Manual controls to start or check the service status  
- 📝 Activity log with timestamps for easy debugging  
- ⚠️ Detects if running without admin rights and warns you (needed for service control)  

---

## 🖥️ Screenshot

![Screenshot](https://github.com/hudulovhamzat0/vgc-guardian/blob/main/ss.png)  
*Dark theme monitoring the VGC service*

---

## 📋 Requirements

- Windows OS (10/11) — **service control commands are Windows-only**  
- Python 3.6 or higher  
- Python packages:
  - `psutil`  
  - `tkinter` (usually included with Python)  
- Must **run as Administrator** to start/stop services successfully  

---

## ⚙️ Installation & Usage

1. Clone or download the repository  
2. Install requirements:
   ```bash
   pip install psutil
Run the application:

bash
Copy
Edit
python app.py
If not running as admin, right-click and select Run as Administrator for full functionality

🎨 Themes
Choose from multiple color themes in the dropdown:

Theme	Preview Colors
Default	Light gray background with black text
Valorant	Dark background with vibrant red highlights
LoL Classic	Deep navy with gold accents
LoL Arcane	Dark slate with cyan highlights
LoL Shadow	Dark blue and beige hues
LoL Spirit	Dark gray and cream

🛡️ License
This project is licensed under the MIT License. Feel free to use and modify it as you wish!

📦 Releases
Download latest releases and binaries from the Releases page
https://github.com/hudulovhamzat0/vgc-guardian/releases

🙌 Contributing
Feel free to submit issues, feature requests, or pull requests!
Please keep code clean and add comments for clarity.

🤝 Acknowledgments
Inspired by the frustration of Vanguard crashes stopping gameplay

Uses psutil for process monitoring

Built with Python & Tkinter for cross-Windows compatibility

Made with ❤️ by Hudulov Hamzat
