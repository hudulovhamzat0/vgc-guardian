🎮 VGC Guardian
🛡️ A friendly Windows GUI tool designed to monitor and automatically restart the VGC service (Riot Vanguard). Perfect for Valorant players tired of unexpected Vanguard crashes stopping their game! 🚀

📺 Demo Video
Check out a quick demo of VGC Guardian in action:

https://youtu.be/CLLMTc7hQCA

✨ Features
Continuous Monitoring: Automatically checks if the VGC service is running in the background.

Auto-Restart: If the VGC service crashes or stops, the guardian will attempt to restart it.

Intuitive GUI: A clean and user-friendly interface with multiple stylish themes to personalize your experience.

Manual Controls: Easily start, stop, restart, or check the VGC service status with dedicated buttons.

Activity Log: A detailed log with timestamps helps you track all actions and troubleshoot issues.

Administrator Warning: Detects if the application is not running with administrator rights and provides a clear warning, as admin privileges are required for service control.

🖥️ Screenshot
VGC Guardian running with a dark theme, monitoring the VGC service.

📋 Requirements
Operating System: Windows 10/11 (Service control commands are Windows-specific).

Python: Version 3.6 or higher.

Python Packages:

psutil: For process and system utility monitoring.

tkinter: The standard Python GUI library (usually included with Python installations).

Administrator Privileges: The application must be run as an Administrator to successfully start, stop, or restart Windows services.

⚙️ Installation & Usage
1. Clone the Repository
First, clone the project to your local machine:

git clone https://github.com/hudulovhamzat0/vgc-guardian.git
cd vgc-guardian

2. Install Dependencies
Install the necessary Python packages using pip:

pip install psutil

(Note: tkinter is typically included with Python, and pyinstaller is only needed if you plan to build an executable.)

3. Run the Application
Execute the main.py script:

python main.py

Important: For full functionality (especially service control), right-click on main.py and select "Run as Administrator," or run your terminal as Administrator before executing the command.

Building an Executable (Optional)
If you want to create a standalone executable (.exe) file for easier distribution, you'll need PyInstaller.

Install PyInstaller:

pip install pyinstaller

Build the Executable:
Navigate to the project root directory in your command prompt and run:

python -m pyinstaller --onefile --windowed --icon=icon.ico --uac-admin main.py

--onefile: Creates a single executable file.

--windowed: Prevents a console window from appearing when the app runs.

--icon=icon.ico: Sets the application icon (ensure icon.ico is in the same directory or provide its full path).

--uac-admin: Prompts for Administrator privileges when the executable is run.

The executable will be generated in the dist folder.

🎨 Themes
VGC Guardian comes with several built-in themes you can switch between from the dropdown menu:

Theme

Preview Colors

Default

Light gray background with black text

Valorant

Dark background with vibrant red highlights

LoL Classic

Deep navy with gold accents

LoL Arcane

Dark slate with cyan highlights

LoL Shadow

Dark blue and beige hues

LoL Spirit

Dark gray and cream

🛡️ License
This project is licensed under the MIT License. Feel free to use and modify it as you wish!

📦 Releases
Download the latest pre-built releases and binaries from the Releases page.

🙌 Contributing
Contributions are welcome! Feel free to submit issues, feature requests, or pull requests. Please ensure your code is clean, well-commented, and follows existing style.

🤝 Acknowledgments
Inspired by the common frustration of Vanguard crashes interrupting gameplay.

Uses psutil for robust process monitoring.

Built with Python & Tkinter for a native Windows GUI experience.

Made with ❤️ by Hudulov Hamzat
