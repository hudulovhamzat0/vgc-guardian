import tkinter as tk
from tkinter import ttk, messagebox
import time
import psutil
import subprocess
import ctypes
import platform
import threading
from datetime import datetime

class VGCMonitorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎮 VGC Service Monitor Pro")
        self.root.geometry("900x850")
        self.root.resizable(False, False)
        
        # Set window icon and style
        self.root.configure(bg="#0d1117")
        
        self.style = ttk.Style()
        self.current_theme = "Gaming Dark"
        
        self.monitoring = False
        self.monitor_thread = None
        self.last_check_time = None
        
        self.is_admin = self.check_admin()
        
        self.setup_themes()
        self.setup_ui()
        self.apply_theme("Gaming Dark")
        self.update_status()
        self.start_auto_refresh()

    def setup_themes(self):
        self.themes = {
            "Gaming Dark": {
                "bg": "#0d1117",
                "fg": "#58a6ff",
                "accent": "#f85149",
                "success": "#3fb950",
                "warning": "#d29922",
                "card_bg": "#161b22",
                "border": "#21262d"
            },
            "Valorant Red": {
                "bg": "#0f1419",
                "fg": "#ff4654",
                "accent": "#ff4654",
                "success": "#53d9d1",
                "warning": "#ffaa3d",
                "card_bg": "#1a1f24",
                "border": "#2a2f35"
            },
            "LoL Gold": {
                "bg": "#010a13",
                "fg": "#c89b3c",
                "accent": "#c89b3c",
                "success": "#0596aa",
                "warning": "#f0e6d2",
                "card_bg": "#1e2328",
                "border": "#3c3c41"
            },
            "Cyberpunk": {
                "bg": "#0a0a0a",
                "fg": "#00f5ff",
                "accent": "#ff0080",
                "success": "#00ff41",
                "warning": "#ffff00",
                "card_bg": "#1a1a1a",
                "border": "#333333"
            },
            "Matrix Green": {
                "bg": "#000000",
                "fg": "#00ff00",
                "accent": "#00ff00",
                "success": "#00ff00",
                "warning": "#ffff00",
                "card_bg": "#0a0a0a",
                "border": "#003300"
            }
        }

    def apply_theme(self, theme_name):
        theme = self.themes[theme_name]
        self.current_theme = theme_name
        
        # Configure root window
        self.root.configure(bg=theme["bg"])
        
        # Configure styles with modern look
        self.style.configure("Card.TFrame", 
                           background=theme["card_bg"], 
                           relief="solid", 
                           borderwidth=1,
                           bd=1)
        
        self.style.configure("Header.TLabel", 
                           background=theme["bg"], 
                           foreground=theme["fg"],
                           font=('Segoe UI', 18, 'bold'))
        
        self.style.configure("Title.TLabel", 
                           background=theme["card_bg"], 
                           foreground=theme["fg"],
                           font=('Segoe UI', 14, 'bold'))
        
        self.style.configure("Status.TLabel", 
                           background=theme["card_bg"], 
                           foreground=theme["fg"],
                           font=('Segoe UI', 11))
        
        self.style.configure("Info.TLabel", 
                           background=theme["card_bg"], 
                           foreground=theme["fg"],
                           font=('Segoe UI', 9))
        
        # Modern button styles
        self.style.configure("Primary.TButton",
                           background=theme["accent"],
                           foreground="white",
                           font=('Segoe UI', 10, 'bold'),
                           borderwidth=0,
                           focuscolor="none")
        
        self.style.map("Primary.TButton",
                      background=[('active', theme["accent"]), ('pressed', theme["accent"])],
                      foreground=[('active', 'white'), ('pressed', 'white')])
        
        self.style.configure("Success.TButton",
                           background=theme["success"],
                           foreground="white",
                           font=('Segoe UI', 10, 'bold'),
                           borderwidth=0,
                           focuscolor="none")
        
        self.style.map("Success.TButton",
                      background=[('active', theme["success"]), ('pressed', theme["success"])],
                      foreground=[('active', 'white'), ('pressed', 'white')])
        
        self.style.configure("Danger.TButton",
                           background="#dc3545",
                           foreground="white",
                           font=('Segoe UI', 10, 'bold'),
                           borderwidth=0,
                           focuscolor="none")
        
        self.style.map("Danger.TButton",
                      background=[('active', '#c82333'), ('pressed', '#bd2130')],
                      foreground=[('active', 'white'), ('pressed', 'white')])
        
        # Combobox style
        self.style.configure("Theme.TCombobox",
                           fieldbackground=theme["card_bg"],
                           background=theme["card_bg"],
                           foreground=theme["fg"],
                           borderwidth=1,
                           relief="solid")
        
        # Update text widget if it exists
        if hasattr(self, 'log_text'):
            self.log_text.configure(
                bg=theme["card_bg"], 
                fg=theme["fg"], 
                insertbackground=theme["fg"],
                selectbackground=theme["accent"],
                selectforeground="white",
                border=0,
                relief="flat"
            )
        
        # Update theme variable
        if hasattr(self, 'theme_var'):
            self.theme_var.set(theme_name)

    def check_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def setup_ui(self):
        # Main container
        main_container = tk.Frame(self.root, bg=self.themes["Gaming Dark"]["bg"])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header section
        header_frame = tk.Frame(main_container, bg=self.themes["Gaming Dark"]["bg"])
        header_frame.pack(fill=tk.X, pady=(0, 30))
        
        # Title with gaming emoji
        title_label = tk.Label(header_frame, 
                              text="🎮 VGC SERVICE MONITOR PRO",
                              font=('Segoe UI', 20, 'bold'),
                              bg=self.themes["Gaming Dark"]["bg"],
                              fg=self.themes["Gaming Dark"]["fg"])
        title_label.pack(side=tk.LEFT)
        
        # Theme selector in header
        theme_frame = tk.Frame(header_frame, bg=self.themes["Gaming Dark"]["bg"])
        theme_frame.pack(side=tk.RIGHT)
        
        theme_label = tk.Label(theme_frame, 
                              text="🎨 Theme:",
                              font=('Segoe UI', 10),
                              bg=self.themes["Gaming Dark"]["bg"],
                              fg=self.themes["Gaming Dark"]["fg"])
        theme_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.theme_var = tk.StringVar(value="Gaming Dark")
        theme_combo = ttk.Combobox(theme_frame, 
                                  textvariable=self.theme_var,
                                  values=list(self.themes.keys()), 
                                  state="readonly", 
                                  width=15,
                                  style="Theme.TCombobox")
        theme_combo.pack(side=tk.LEFT)
        theme_combo.bind("<<ComboboxSelected>>", self.on_theme_change)
        
        # Status card
        status_card = tk.Frame(main_container, 
                              bg=self.themes["Gaming Dark"]["card_bg"],
                              relief="solid",
                              bd=1)
        status_card.pack(fill=tk.X, pady=(0, 20))
        
        status_header = tk.Frame(status_card, bg=self.themes["Gaming Dark"]["card_bg"])
        status_header.pack(fill=tk.X, padx=20, pady=(15, 0))
        
        status_title = tk.Label(status_header,
                               text="⚡ SERVICE STATUS",
                               font=('Segoe UI', 14, 'bold'),
                               bg=self.themes["Gaming Dark"]["card_bg"],
                               fg=self.themes["Gaming Dark"]["fg"])
        status_title.pack(side=tk.LEFT)
        
        status_content = tk.Frame(status_card, bg=self.themes["Gaming Dark"]["card_bg"])
        status_content.pack(fill=tk.X, padx=20, pady=20)
        
        self.service_status_var = tk.StringVar(value="🔄 Checking...")
        self.service_status_label = tk.Label(status_content,
                                            textvariable=self.service_status_var,
                                            font=('Segoe UI', 16, 'bold'),
                                            bg=self.themes["Gaming Dark"]["card_bg"],
                                            fg=self.themes["Gaming Dark"]["success"])
        self.service_status_label.pack(anchor=tk.W)
        
        self.last_check_var = tk.StringVar(value="Never")
        last_check_label = tk.Label(status_content,
                                   text="🕒 Last Check: ",
                                   font=('Segoe UI', 10),
                                   bg=self.themes["Gaming Dark"]["card_bg"],
                                   fg=self.themes["Gaming Dark"]["fg"])
        last_check_label.pack(anchor=tk.W, pady=(10, 0))
        
        last_check_time_label = tk.Label(status_content,
                                        textvariable=self.last_check_var,
                                        font=('Segoe UI', 10),
                                        bg=self.themes["Gaming Dark"]["card_bg"],
                                        fg=self.themes["Gaming Dark"]["warning"])
        last_check_time_label.pack(anchor=tk.W)
        
        # Monitor control card
        monitor_card = tk.Frame(main_container,
                               bg=self.themes["Gaming Dark"]["card_bg"],
                               relief="solid",
                               bd=1)
        monitor_card.pack(fill=tk.X, pady=(0, 20))
        
        monitor_header = tk.Frame(monitor_card, bg=self.themes["Gaming Dark"]["card_bg"])
        monitor_header.pack(fill=tk.X, padx=20, pady=(15, 0))
        
        monitor_title = tk.Label(monitor_header,
                                text="🤖 AUTO MONITOR",
                                font=('Segoe UI', 14, 'bold'),
                                bg=self.themes["Gaming Dark"]["card_bg"],
                                fg=self.themes["Gaming Dark"]["fg"])
        monitor_title.pack(side=tk.LEFT)
        
        monitor_content = tk.Frame(monitor_card, bg=self.themes["Gaming Dark"]["card_bg"])
        monitor_content.pack(fill=tk.X, padx=20, pady=20)
        
        self.monitor_status_var = tk.StringVar(value="💤 Stopped")
        monitor_status_label = tk.Label(monitor_content,
                                       textvariable=self.monitor_status_var,
                                       font=('Segoe UI', 12, 'bold'),
                                       bg=self.themes["Gaming Dark"]["card_bg"],
                                       fg=self.themes["Gaming Dark"]["fg"])
        monitor_status_label.pack(anchor=tk.W, pady=(0, 15))
        
        button_frame = tk.Frame(monitor_content, bg=self.themes["Gaming Dark"]["card_bg"])
        button_frame.pack(fill=tk.X)
        
        self.start_button = ttk.Button(button_frame, 
                                      text="🚀 START MONITORING",
                                      command=self.start_monitoring,
                                      style="Success.TButton",
                                      width=20)
        self.start_button.pack(side=tk.LEFT, padx=(0, 15))
        
        self.stop_button = ttk.Button(button_frame, 
                                     text="🛑 STOP MONITORING",
                                     command=self.stop_monitoring,
                                     state=tk.DISABLED,
                                     style="Danger.TButton",
                                     width=20)
        self.stop_button.pack(side=tk.LEFT)
        
        # Manual control card
        control_card = tk.Frame(main_container,
                               bg=self.themes["Gaming Dark"]["card_bg"],
                               relief="solid",
                               bd=1)
        control_card.pack(fill=tk.X, pady=(0, 20))
        
        control_header = tk.Frame(control_card, bg=self.themes["Gaming Dark"]["card_bg"])
        control_header.pack(fill=tk.X, padx=20, pady=(15, 0))
        
        control_title = tk.Label(control_header,
                                text="🎛️ MANUAL CONTROLS",
                                font=('Segoe UI', 14, 'bold'),
                                bg=self.themes["Gaming Dark"]["card_bg"],
                                fg=self.themes["Gaming Dark"]["fg"])
        control_title.pack(side=tk.LEFT)
        
        control_content = tk.Frame(control_card, bg=self.themes["Gaming Dark"]["card_bg"])
        control_content.pack(fill=tk.X, padx=20, pady=20)
        
        # Control buttons grid
        button_grid = tk.Frame(control_content, bg=self.themes["Gaming Dark"]["card_bg"])
        button_grid.pack(fill=tk.X)
        
        # Row 1
        row1 = tk.Frame(button_grid, bg=self.themes["Gaming Dark"]["card_bg"])
        row1.pack(fill=tk.X, pady=(0, 10))
        
        self.start_service_button = ttk.Button(row1, 
                                              text="▶️ START VGC",
                                              command=self.manual_start_service, 
                                              style="Success.TButton", 
                                              width=18)
        self.start_service_button.pack(side=tk.LEFT, padx=(0, 15))
        
        self.restart_service_button = ttk.Button(row1, 
                                                text="🔄 RESTART VGC",
                                                command=self.manual_restart_service, 
                                                style="Primary.TButton", 
                                                width=18)
        self.restart_service_button.pack(side=tk.LEFT, padx=(0, 15))
        
        # Row 2
        row2 = tk.Frame(button_grid, bg=self.themes["Gaming Dark"]["card_bg"])
        row2.pack(fill=tk.X)
        
        self.stop_service_button = ttk.Button(row2, 
                                             text="⏹️ STOP VGC",
                                             command=self.manual_stop_service, 
                                             style="Danger.TButton", 
                                             width=18)
        self.stop_service_button.pack(side=tk.LEFT, padx=(0, 15))
        
        self.check_service_button = ttk.Button(row2, 
                                              text="🔍 CHECK STATUS",
                                              command=self.manual_check_service, 
                                              style="Primary.TButton", 
                                              width=18)
        self.check_service_button.pack(side=tk.LEFT)
        
        # Log card
        log_card = tk.Frame(main_container,
                           bg=self.themes["Gaming Dark"]["card_bg"],
                           relief="solid",
                           bd=1)
        log_card.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        log_header = tk.Frame(log_card, bg=self.themes["Gaming Dark"]["card_bg"])
        log_header.pack(fill=tk.X, padx=20, pady=(15, 0))
        
        log_title = tk.Label(log_header,
                            text="📋 ACTIVITY LOG",
                            font=('Segoe UI', 14, 'bold'),
                            bg=self.themes["Gaming Dark"]["card_bg"],
                            fg=self.themes["Gaming Dark"]["fg"])
        log_title.pack(side=tk.LEFT)
        
        log_content = tk.Frame(log_card, bg=self.themes["Gaming Dark"]["card_bg"])
        log_content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Log text with scrollbar
        log_container = tk.Frame(log_content, bg=self.themes["Gaming Dark"]["card_bg"])
        log_container.pack(fill=tk.BOTH, expand=True)
        
        self.log_text = tk.Text(log_container, 
                               height=12, 
                               font=('Consolas', 10), 
                               wrap=tk.WORD,
                               bg=self.themes["Gaming Dark"]["card_bg"],
                               fg=self.themes["Gaming Dark"]["fg"],
                               insertbackground=self.themes["Gaming Dark"]["fg"],
                               selectbackground=self.themes["Gaming Dark"]["accent"],
                               selectforeground="white",
                               border=0,
                               relief="flat")
        
        scrollbar = ttk.Scrollbar(log_container, orient=tk.VERTICAL, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Admin warning
        if not self.is_admin:
            warning_card = tk.Frame(main_container,
                                   bg="#dc3545",
                                   relief="solid",
                                   bd=1)
            warning_card.pack(fill=tk.X, pady=(10, 0))
            
            warning_label = tk.Label(warning_card,
                                    text="⚠️ WARNING: Not running as Administrator - Service control may fail",
                                    font=('Segoe UI', 11, 'bold'),
                                    fg="white",
                                    bg="#dc3545")
            warning_label.pack(pady=15)
        
        # Initialize log
        self.log_message("🎮 VGC Monitor Pro initialized")
        if not self.is_admin:
            self.log_message("⚠️ WARNING: Not running as Administrator")
        self.log_message("🚀 Ready for gaming!")

    def on_theme_change(self, event=None):
        selected_theme = self.theme_var.get()
        self.apply_theme(selected_theme)
        self.log_message(f"🎨 Theme changed to: {selected_theme}")

    def log_message(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        
        # Keep log manageable
        if self.log_text.index(tk.END + "-1c").split('.')[0] == "200":
            self.log_text.delete("1.0", "50.0")

    def is_vgc_running(self):
        try:
            result = subprocess.run(["sc", "query", "vgc"],
                                  capture_output=True, text=True, shell=True)
            
            if result.returncode == 0:
                output = result.stdout.lower()
                if "running" in output:
                    return True
                elif "stopped" in output:
                    return False
            
            for process in psutil.process_iter(['name']):
                if process.info['name'] and 'vgc' in process.info['name'].lower():
                    return True
            return False
        except Exception as e:
            self.log_message(f"❌ Error checking VGC status: {e}")
            return False

    def start_vgc_service(self):
        try:
            self.log_message("🚀 Attempting to start VGC service...")
            result = subprocess.run(["sc", "start", "vgc"],
                                  capture_output=True, text=True, shell=True)
            
            if result.returncode == 0:
                self.log_message("✅ VGC service start command sent successfully")
                return True
            else:
                self.log_message(f"❌ Failed to start VGC service: {result.stderr}")
                return False
                
        except Exception as e:
            self.log_message(f"❌ Error starting VGC service: {e}")
            return False

    def stop_vgc_service(self):
        try:
            self.log_message("⏹️ Attempting to stop VGC service...")
            result = subprocess.run(["sc", "stop", "vgc"],
                                  capture_output=True, text=True, shell=True)
            
            if result.returncode == 0:
                self.log_message("✅ VGC service stop command sent successfully")
                return True
            else:
                self.log_message(f"❌ Failed to stop VGC service: {result.stderr}")
                return False
                
        except Exception as e:
            self.log_message(f"❌ Error stopping VGC service: {e}")
            return False

    def restart_vgc_service(self):
        self.log_message("🔄 Restarting VGC service...")
        
        if self.is_vgc_running():
            if not self.stop_vgc_service():
                return False
            time.sleep(2)
        
        return self.start_vgc_service()

    def update_status(self):
        if platform.system() != "Windows":
            self.service_status_var.set("❌ Windows Only")
            return
        
        is_running = self.is_vgc_running()
        self.last_check_time = datetime.now()
        self.last_check_var.set(self.last_check_time.strftime("%H:%M:%S"))
        
        if is_running:
            self.service_status_var.set("✅ VGC is Running")
        else:
            self.service_status_var.set("❌ VGC is Not Running")
        
        return is_running

    def monitor_loop(self):
        while self.monitoring:
            try:
                self.root.after(0, self.update_status)
                is_running = self.is_vgc_running()
                
                if not is_running:
                    self.root.after(0, lambda: self.log_message("⚠️ VGC service not running - attempting to start"))
                    if self.start_vgc_service():
                        time.sleep(2)
                        if self.is_vgc_running():
                            self.root.after(0, lambda: self.log_message("🎉 VGC service started successfully"))
                        else:
                            self.root.after(0, lambda: self.log_message("⚠️ VGC service start may have failed"))
                
                time.sleep(1)
                
            except Exception as e:
                self.root.after(0, lambda: self.log_message(f"❌ Monitor loop error: {e}"))
                time.sleep(5)

    def start_monitoring(self):
        if platform.system() != "Windows":
            messagebox.showerror("Error", "This application only works on Windows")
            return
        
        self.monitoring = True
        self.monitor_status_var.set("🤖 Running")
        
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        
        self.monitor_thread = threading.Thread(target=self.monitor_loop, daemon=True)
        self.monitor_thread.start()
        
        self.log_message("🤖 Monitoring started - checking every 1 second")

    def stop_monitoring(self):
        self.monitoring = False
        self.monitor_status_var.set("💤 Stopped")
        
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        
        self.log_message("💤 Monitoring stopped")

    def manual_start_service(self):
        if self.start_vgc_service():
            messagebox.showinfo("Success", "✅ VGC service start command sent")
        else:
            messagebox.showerror("Error", "❌ Failed to start VGC service")

    def manual_stop_service(self):
        if self.stop_vgc_service():
            messagebox.showinfo("Success", "✅ VGC service stop command sent")
        else:
            messagebox.showerror("Error", "❌ Failed to stop VGC service")

    def manual_restart_service(self):
        if self.restart_vgc_service():
            messagebox.showinfo("Success", "🎉 VGC service restarted successfully")
        else:
            messagebox.showerror("Error", "❌ Failed to restart VGC service")

    def manual_check_service(self):
        self.update_status()
        is_running = self.is_vgc_running()
        status = "running" if is_running else "not running"
        icon = "✅" if is_running else "❌"
        messagebox.showinfo("Service Status", f"{icon} VGC service is {status}")

    def run(self):
        try:
            self.update_status()
            self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.root.mainloop()
            
        except Exception as e:
            messagebox.showerror("Error", f"Application error: {e}")

    def on_closing(self):
        if self.monitoring:
            self.stop_monitoring()
        self.root.destroy()

    def start_auto_refresh(self):
        if not self.monitoring:
            self.update_status()
        self.root.after(2000, self.start_auto_refresh)

def main():
    app = VGCMonitorGUI()
    app.run()

if __name__ == "__main__":
    main()