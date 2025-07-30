<h1 id="vgc-guardian">🎮 VGC Guardian</h1>
<blockquote>
<p>🛡️ A friendly Windows GUI tool designed to <strong>monitor</strong> and <strong>automatically restart</strong> the <strong>VGC service</strong> (Riot Vanguard). Perfect for Valorant players tired of unexpected Vanguard crashes stopping their game! 🚀</p>
</blockquote>
<hr />
<p><a href="https://www.microsoft.com/windows/"><img src="https://img.shields.io/badge/Platform-Windows-blue.svg" alt="Windows" /></a>
<a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.6%2B-green.svg" alt="Python" /></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="License" /></a>
<a href="https://youtu.be/CLLMTc7hQCA"><img src="https://img.shields.io/badge/Demo-YouTube-red.svg?logo=youtube" alt="YouTube Demo" /></a></p>
<hr />
<h2 id="demo-video">📺 Demo Video</h2>
<p>Check out a quick demo of VGC Guardian in action:</p>
<p><a href="https://youtu.be/CLLMTc7hQCA">https://youtu.be/CLLMTc7hQCA</a></p>
<h2 id="features">✨ Features</h2>
<ul>
<li><strong>Continuous Monitoring</strong>: Automatically checks if the VGC service is running in the background.</li>
<li><strong>Auto-Restart</strong>: If the VGC service crashes or stops, the guardian will attempt to restart it.</li>
<li><strong>Intuitive GUI</strong>: A clean and user-friendly interface with multiple stylish themes to personalize your experience.</li>
<li><strong>Manual Controls</strong>: Easily start, stop, restart, or check the VGC service status with dedicated buttons.</li>
<li><strong>Activity Log</strong>: A detailed log with timestamps helps you track all actions and troubleshoot issues.</li>
<li><strong>Administrator Warning</strong>: Detects if the application is not running with administrator rights and provides a clear warning, as admin privileges are required for service control.</li>
</ul>
<hr />
<h2 id="screenshot">🖥️ Screenshot</h2>
<p><img src="https://github.com/hudulovhamzat0/vgc-guardian/blob/main/ss.png" alt="Screenshot of VGC Guardian" /></p>
<p><em>VGC Guardian running with a dark theme, monitoring the VGC service.</em></p>
<hr />
<h2 id="requirements">📋 Requirements</h2>
<ul>
<li><strong>Operating System</strong>: Windows 10/11 (Service control commands are Windows-specific).</li>
<li><strong>Python</strong>: Version 3.6 or higher.</li>
<li><strong>Python Packages</strong>:
<ul>
<li><code>psutil</code>: For process and system utility monitoring.</li>
<li><code>tkinter</code>: The standard Python GUI library (usually included with Python installations).</li>
</ul>
</li>
<li><strong>Administrator Privileges</strong>: The application <strong>must be run as an Administrator</strong> to successfully start, stop, or restart Windows services.</li>
</ul>
<hr />
<h2 id="installation--usage">⚙️ Installation &amp; Usage</h2>
<h3 id="1-clone-the-repository">1. Clone the Repository</h3>
<p>First, clone the project to your local machine:</p>
<pre><code class="language-bash">git clone https://github.com/hudulovhamzat0/vgc-guardian.git
cd vgc-guardian
</code></pre>
<h3 id="2-install-dependencies">2. Install Dependencies</h3>
<p>Install the necessary Python packages using pip:</p>
<pre><code class="language-bash">pip install psutil
</code></pre>
<p><em>(Note: <code>tkinter</code> is typically included with Python, and <code>pyinstaller</code> is only needed if you plan to build an executable.)</em></p>
<h3 id="3-run-the-application">3. Run the Application</h3>
<p>Execute the <code>main.py</code> script:</p>
<pre><code class="language-bash">python main.py
</code></pre>
<p><strong>Important</strong>: For full functionality (especially service control), right-click on <code>main.py</code> and select &quot;Run as Administrator,&quot; or run your terminal as Administrator before executing the command.</p>
<h3 id="building-an-executable-optional">Building an Executable (Optional)</h3>
<p>If you want to create a standalone executable (<code>.exe</code>) file for easier distribution, you'll need <code>PyInstaller</code>.</p>
<ol>
<li><strong>Install PyInstaller</strong>:
<pre><code class="language-bash">pip install pyinstaller
</code></pre>
</li>
<li><strong>Build the Executable</strong>:
<p>Navigate to the project root directory in your command prompt and run:</p>
<pre><code class="language-cmd">python -m pyinstaller --onefile --windowed --icon=icon.ico --uac-admin main.py
</code></pre>
<ul>
<li><code>--onefile</code>: Creates a single executable file.</li>
<li><code>--windowed</code>: Prevents a console window from appearing when the app runs.</li>
<li><code>--icon=icon.ico</code>: Sets the application icon (ensure <code>icon.ico</code> is in the same directory or provide its full path).</li>
<li><code>--uac-admin</code>: Prompts for Administrator privileges when the executable is run.</li>
</ul>
<p>The executable will be generated in the <code>dist</code> folder.</p>
</li>
</ol>
<hr />
<h2 id="themes">🎨 Themes</h2>
<p>VGC Guardian comes with several built-in themes you can switch between from the dropdown menu:</p>
<table>
<thead>
<tr>
<th>Theme</th>
<th>Preview Colors</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Default</code></td>
<td>Light gray background with black text</td>
</tr>
<tr>
<td><code>Valorant</code></td>
<td>Dark background with vibrant red highlights</td>
</tr>
<tr>
<td><code>LoL Classic</code></td>
<td>Deep navy with gold accents</td>
</tr>
<tr>
<td><code>LoL Arcane</code></td>
<td>Dark slate with cyan highlights</td>
</tr>
<tr>
<td><code>LoL Shadow</code></td>
<td>Dark blue and beige hues</td>
</tr>
<tr>
<td><code>LoL Spirit</code></td>
<td>Dark gray and cream</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="license">🛡️ License</h2>
<p>This project is licensed under the <a href="https://www.google.com/search?q=MIT+License">MIT License</a>. Feel free to use and modify it as you wish!</p>
<hr />
<h2 id="releases">📦 Releases</h2>
<p>Download the latest pre-built releases and binaries from the <a href="https://github.com/hudulovhamzat0/vgc-guardian/releases">Releases page</a>.</p>
<hr />
<h2 id="contributing">🙌 Contributing</h2>
<p>Contributions are welcome! Feel free to submit issues, feature requests, or pull requests. Please ensure your code is clean, well-commented, and follows existing style.</p>
<hr />
<h2 id="acknowledgments">🤝 Acknowledgments</h2>
<ul>
<li>Inspired by the common frustration of Vanguard crashes interrupting gameplay.</li>
<li>Uses <code>psutil</code> for robust process monitoring.</li>
<li>Built with Python &amp; Tkinter for a native Windows GUI experience.</li>
</ul>
<p>Made with ❤️ by Hudulov Hamzat</p>
