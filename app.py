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
        self.root.title("VGC Service Monitor")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        
        self.style = ttk.Style()
        self.current_theme = "Default"
        
        self.monitoring = False
        self.monitor_thread = None
        self.last_check_time = None
        
        self.is_admin = self.check_admin()
        
        self.setup_themes()
        self.setup_ui()
        self.apply_theme("Default")
        self.update_status()
        
    def setup_themes(self):
        self.themes = {
            "Default": {
                "bg": "#f0f0f0",
                "fg": "#000000",
                "select_bg": "#0078d4",
                "select_fg": "#ffffff"
            },
            "Valorant": {
                "bg": "#0f1419",
                "fg": "#ff4654",
                "select_bg": "#ff4654",
                "select_fg": "#0f1419"
            },
            "LoL Classic": {
                "bg": "#010a13",
                "fg": "#c89b3c",
                "select_bg": "#c89b3c",
                "select_fg": "#010a13"
            },
            "LoL Arcane": {
                "bg": "#1e2328",
                "fg": "#00f5ff",
                "select_bg": "#00f5ff",
                "select_fg": "#1e2328"
            },
            "LoL Shadow": {
                "bg": "#0a1428",
                "fg": "#cdbe91",
                "select_bg": "#463714",
                "select_fg": "#cdbe91"
            },
            "LoL Spirit": {
                "bg": "#1e1e1e",
                "fg": "#f0e6d2",
                "select_bg": "#785a28",
                "select_fg": "#f0e6d2"
            }
        }
    
    def apply_theme(self, theme_name):
        theme = self.themes[theme_name]
        self.current_theme = theme_name
        
        self.root.configure(bg=theme["bg"])
        
        self.style.configure("Themed.TFrame", background=theme["bg"])
        self.style.configure("Themed.TLabel", background=theme["bg"], foreground=theme["fg"])
        self.style.configure("Themed.TLabelframe", background=theme["bg"], foreground=theme["fg"])
        self.style.configure("Themed.TLabelframe.Label", background=theme["bg"], foreground=theme["fg"])
        self.style.configure("Themed.TButton", background=theme["select_bg"], foreground=theme["select_fg"])
        
        if theme_name == "Default":
            self.style.configure("Success.TButton", background="#28a745", foreground="white")
            self.style.configure("Danger.TButton", background="#dc3545", foreground="white")
        else:
            self.style.configure("Success.TButton", background="#28a745", foreground="white")
            self.style.configure("Danger.TButton", background="#dc3545", foreground="white")
        
        self.style.map("Success.TButton", 
                      background=[('active', '#218838'), ('pressed', '#1e7e34')])
        self.style.map("Danger.TButton", 
                      background=[('active', '#c82333'), ('pressed', '#bd2130')])
        
        if hasattr(self, 'log_text'):
            self.log_text.configure(bg=theme["bg"], fg=theme["fg"], insertbackground=theme["fg"])
        
        if hasattr(self, 'start_button'):
            self.start_button.configure(style="Success.TButton")
        if hasattr(self, 'stop_button'):
            self.stop_button.configure(style="Danger.TButton")
        
        self.theme_var.set(theme_name)
    
    def check_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    def setup_ui(self):
        theme_frame = ttk.Frame(self.root, style="Themed.TFrame")
        theme_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(theme_frame, text="Theme:", style="Themed.TLabel").pack(side=tk.LEFT)
        
        self.theme_var = tk.StringVar(value="Default")
        theme_combo = ttk.Combobox(theme_frame, textvariable=self.theme_var, 
                                  values=list(self.themes.keys()), state="readonly", width=12)
        theme_combo.pack(side=tk.LEFT, padx=(5, 0))
        theme_combo.bind("<<ComboboxSelected>>", self.on_theme_change)
        
        main_frame = ttk.Frame(self.root, padding="20", style="Themed.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title_label = ttk.Label(main_frame, text="VGC Service Monitor", 
                               font=('Segoe UI', 16, 'bold'), style="Themed.TLabel")
        title_label.pack(pady=(0, 20))
        
        status_frame = ttk.LabelFrame(main_frame, text="Service Status", padding="15", style="Themed.TLabelframe")
        status_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.service_status_var = tk.StringVar(value="Checking...")
        self.service_status_label = ttk.Label(status_frame, 
                                            textvariable=self.service_status_var,
                                            font=('Segoe UI', 12, 'bold'), style="Themed.TLabel")
        self.service_status_label.pack()
        
        self.last_check_var = tk.StringVar(value="Never")
        last_check_label = ttk.Label(status_frame, 
                                   text="Last Check: ",
                                   font=('Segoe UI', 9), style="Themed.TLabel")
        last_check_label.pack(anchor=tk.W, pady=(10, 0))
        
        last_check_time_label = ttk.Label(status_frame, 
                                        textvariable=self.last_check_var,
                                        font=('Segoe UI', 9), style="Themed.TLabel")
        last_check_time_label.pack(anchor=tk.W)
        
        monitor_frame = ttk.LabelFrame(main_frame, text="Monitor Control", padding="15", style="Themed.TLabelframe")
        monitor_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.monitor_status_var = tk.StringVar(value="Stopped")
        monitor_status_label = ttk.Label(monitor_frame, 
                                       text="Monitor Status: ",
                                       font=('Segoe UI', 10), style="Themed.TLabel")
        monitor_status_label.pack(anchor=tk.W)
        
        self.monitor_status_display = ttk.Label(monitor_frame, 
                                              textvariable=self.monitor_status_var,
                                              font=('Segoe UI', 10, 'bold'), style="Themed.TLabel")
        self.monitor_status_display.pack(anchor=tk.W, pady=(0, 10))
        
        button_frame = ttk.Frame(monitor_frame, style="Themed.TFrame")
        button_frame.pack(fill=tk.X)
        
        self.start_button = ttk.Button(button_frame, text="Start Monitoring", 
                                     command=self.start_monitoring,
                                     style="Success.TButton")
        self.start_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.stop_button = ttk.Button(button_frame, text="Stop Monitoring", 
                                    command=self.stop_monitoring,
                                    state=tk.DISABLED,
                                    style="Danger.TButton")
        self.stop_button.pack(side=tk.LEFT)
        
        service_frame = ttk.LabelFrame(main_frame, text="Manual Service Control", padding="15", style="Themed.TLabelframe")
        service_frame.pack(fill=tk.X, pady=(0, 15))
        
        service_button_frame = ttk.Frame(service_frame, style="Themed.TFrame")
        service_button_frame.pack(fill=tk.X)
        
        self.start_service_button = ttk.Button(service_button_frame, text="Start VGC Service", 
                                             command=self.manual_start_service, style="Themed.TButton")
        self.start_service_button.pack(side=tk.LEFT, padx=(0, 10))
        
        self.check_service_button = ttk.Button(service_button_frame, text="Check Service", 
                                             command=self.manual_check_service, style="Themed.TButton")
        self.check_service_button.pack(side=tk.LEFT)
        
        log_frame = ttk.LabelFrame(main_frame, text="Activity Log", padding="10", style="Themed.TLabelframe")
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        log_container = ttk.Frame(log_frame, style="Themed.TFrame")
        log_container.pack(fill=tk.BOTH, expand=True)
        
        self.log_text = tk.Text(log_container, height=8, width=50, 
                               font=('Consolas', 9), wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(log_container, orient=tk.VERTICAL, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        if not self.is_admin:
            warning_frame = ttk.Frame(main_frame, style="Themed.TFrame")
            warning_frame.pack(fill=tk.X, pady=(10, 0))
            
            warning_label = ttk.Label(warning_frame, 
                                    text="⚠️ Not running as Administrator - Service control may fail",
                                    foreground="red",
                                    font=('Segoe UI', 9), style="Themed.TLabel")
            warning_label.pack()
        
        self.log_message("VGC Monitor initialized")
        if not self.is_admin:
            self.log_message("WARNING: Not running as Administrator")
    
    def on_theme_change(self, event=None):
        selected_theme = self.theme_var.get()
        self.apply_theme(selected_theme)
        self.log_message(f"Theme changed to: {selected_theme}")
        
    def log_message(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        
        if self.log_text.index(tk.END + "-1c").split('.')[0] == "200":
            self.log_text.delete("1.0", "50.0")
    
    def is_vgc_running(self):
        try:
            for process in psutil.process_iter(['name']):
                if process.info['name'] and 'vgc' in process.info['name'].lower():
                    return True
            return False
        except Exception as e:
            self.log_message(f"Error checking VGC status: {e}")
            return False
    
    def start_vgc_service(self):
        try:
            self.log_message("Attempting to start VGC service...")
            result = subprocess.run(["sc", "start", "vgc"], 
                                  capture_output=True, text=True, shell=True)
            
            if result.returncode == 0:
                self.log_message("VGC service start command sent successfully")
                return True
            else:
                self.log_message(f"Failed to start VGC service: {result.stderr}")
                return False
                
        except Exception as e:
            self.log_message(f"Error starting VGC service: {e}")
            return False
    
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
                is_running = self.update_status()
                
                if not is_running:
                    self.log_message("VGC service not running - attempting to start")
                    if self.start_vgc_service():
                        time.sleep(2)
                        if self.is_vgc_running():
                            self.log_message("VGC service started successfully")
                        else:
                            self.log_message("VGC service start may have failed")
                
                time.sleep(1)
                
            except Exception as e:
                self.log_message(f"Monitor loop error: {e}")
                time.sleep(5)
    
    def start_monitoring(self):
        if platform.system() != "Windows":
            messagebox.showerror("Error", "This application only works on Windows")
            return
        
        self.monitoring = True
        self.monitor_status_var.set("Running")
        
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        
        self.monitor_thread = threading.Thread(target=self.monitor_loop, daemon=True)
        self.monitor_thread.start()
        
        self.log_message("Monitoring started - checking every 1 second")
    
    def stop_monitoring(self):
        self.monitoring = False
        self.monitor_status_var.set("Stopped")
        
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        
        self.log_message("Monitoring stopped")
    
    def manual_start_service(self):
        if self.start_vgc_service():
            messagebox.showinfo("Success", "VGC service start command sent")
        else:
            messagebox.showerror("Error", "Failed to start VGC service")
    
    def manual_check_service(self):
        self.update_status()
        is_running = self.is_vgc_running()
        status = "running" if is_running else "not running"
        messagebox.showinfo("Service Status", f"VGC service is {status}")
    
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

def main():
    app = VGCMonitorGUI()
    app.run()

if __name__ == "__main__":
    main()