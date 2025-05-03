# osu!Collector Downloader

A GUI application made in Python to download beatmaps from osucollector.com

## Getting Started
First off, you need the osu!collector ID. You can obtain one from the address bar of your web browser.

### On Windows
Simply grab the [latest release](https://github.com/scruffiebaka/osuCollector-Downloader/releases/latest) and run it.
Enter a the osu!collector ID along with the downloads location.
Click on Download, if ratelimit is hit then the program would go on standby for a minute or two. 
Currently its using catboy.best mirror but I plan on adding more.

### Building on windows
1. Clone the repository
   ```sh
   git clone https://github.com/scruffiebaka/osuCollector-Downloader.git
   cd osuCollector-Downloader
   ```
2. Make sure you have python 3.13 >= installed
2. Install the requirements by running
   ```sh
   pip install -r requirements.txt
   ```
3. Run the program using
   ```sh
   python3 main.py
   ```

### On UNIX
1. Clone the repository
   ```sh
   git clone https://github.com/scruffiebaka/osuCollector-Downloader.git
   cd osuCollector-Downloader
   ```
2. Make sure you have python 3.13 >= installed

   On MacOS, simply use pip to install the requirements
   ```sh
   pip install -r requirements.txt
   ```
   On Linux distros, you need to use your package manager to get python-requests, tkinter and pillow

3. Run the program using
   ```sh
   python3 main.py
   ```

## Todo:
1. Implement different mirrors
2. Rework on the GUI
