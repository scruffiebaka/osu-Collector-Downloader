import os
import window
import helper
import requestor

# Create download folder on start
if(os.path.exists(helper.resource_path("Downloads")) == False):
    os.mkdir(helper.resource_path("Downloads"))

window.default_location = helper.resource_path("Downloads")

window.init_window(requestor.init_downloader)