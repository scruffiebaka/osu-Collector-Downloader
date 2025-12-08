import os
import sys
import window
import requestor

if getattr(sys, 'frozen', False):
    app_dir = os.path.dirname(sys.executable)
else:
    app_dir = os.path.dirname(os.path.abspath(__file__))

download_dir = os.path.join(app_dir, "Downloads")
os.makedirs(download_dir, exist_ok=True)

window.default_location = download_dir

window.init_window(requestor.init_downloader)
