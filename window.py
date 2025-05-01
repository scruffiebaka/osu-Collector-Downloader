import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from helper import resource_path

id_var = None 
location_var = None
button = None

def init_window(callback):
    # Initialize Window
    window = tk.Tk()
    window.title("osu!Collector Downloader")
    window.resizable(width=False, height=False)
    
    # Set variables
    global button, id_var, location_var
    id_var = tk.StringVar()
    location_var = tk.StringVar()
    
    # Set the canvas
    canvas = tk.Canvas(window, width=640, height=420)
    canvas.pack()
    
    # Set the icon
    icon = tk.PhotoImage(file=resource_path("assets/icon.png"))
    window.iconphoto(False, icon)
    
    # Set all elements
    set_labels(window=window)
    set_entries(window=window)
    
    # Set the button
    button = tk.Button(text="Download", command=lambda: callback(id_var.get(), location_var.get()))
    button.place(x=500,y=130)
    
    # Start the main loop
    window.mainloop()

def set_labels(window):
    welcome_label=tk.Label(window)
    welcome_label["anchor"] = "e"
    ft = tkFont.Font(family='Arial',size=16)
    welcome_label["font"] = ft
    welcome_label["fg"] = "#333333"
    welcome_label["justify"] = "left"
    welcome_label["text"] = "Welcome to osu!Collector Downloader!"
    welcome_label.place(x=-120,y=10,width=640,height=50)
    
    # Info labels
    beatmapid_label=tk.Label(window)
    beatmapid_label["anchor"] = "e"
    ft = tkFont.Font(family='Arial',size=14)
    beatmapid_label["font"] = ft
    beatmapid_label["fg"] = "#333333"
    beatmapid_label["justify"] = "center"
    beatmapid_label["text"] = "Beatmapset ID:"
    beatmapid_label.place(x=10,y=75,width=130,height=50)
    
    downloadlocation_label=tk.Label(window)
    downloadlocation_label["anchor"] = "e"
    ft = tkFont.Font(family='Arial',size=14)
    downloadlocation_label["font"] = ft
    downloadlocation_label["fg"] = "#333333"
    downloadlocation_label["justify"] = "center"
    downloadlocation_label["text"] = "Download location:"
    downloadlocation_label.place(x=10,y=125,width=156,height=50)

def set_entries(window):
    beatmapid=tk.Entry(window, textvariable=id_var)
    beatmapid.place(x=200,y=82,width=100,height=30)
    
    downloadlocation=tk.Entry(window, textvariable=location_var)
    downloadlocation.place(x=200,y=132,width=250,height=30)

def disable_button():
    button.config(state="disabled")

def enable_button():
    button.config(state="active")

def warning(infotext):
    infobox = messagebox.showwarning(title="Warning", message=infotext)
    
def error(errortext, callback):
    errorbox = messagebox.showerror(title="Error!", message=errortext)
    if(errorbox):
        callback()