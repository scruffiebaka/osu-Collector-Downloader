import threading
import tkinter
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar, ttk, messagebox
from helper import resource_path

default_location = None

id_var = None
location_var = None
button = None
progress = 0

canvas = None

setname_text = None
name_text = None
size_text = None
progress_text = None
speed_text = None

def init_window(callback):
    
    # Initialize Window
    window = Tk()
    window.title("osu!Collector Downloader")
    window.geometry("640x420")
    window.configure(bg = "#FEEAFF")
    
    global id_var, location_var, button, progress, canvas, setname_text, name_text, size_text, progress_text, speed_text
    id_var = StringVar()
    location_var = StringVar()
    
    canvas = Canvas(
        window,
        bg = "#FEEAFF",
        height = 420,
        width = 640,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)
    
    canvas.create_text(
        50.0,
        21.0,
        anchor="nw",
        text="Welcome to osu!collector Downloader!",
        fill="#2F2F2F",
        font=("Roboto Regular", 30 * -1)
    )
    
    canvas.create_text(
        16.0,
        134.0,
        anchor="nw",
        text="osu!collector ID:",
        fill="#2F2F2F",
        font=("Roboto Regular", 20 * -1)
    )
    
    canvas.create_text(
        16.0,
        174.0,
        anchor="nw",
        text="Download location:",
        fill="#2F2F2F",
        font=("Roboto Regular", 20 * -1)
    )
    
    setname_text = canvas.create_text(
        16.0,
        216.0,
        anchor="nw",
        text="Downloading: ",
        fill="#2F2F2F",
        font=("Roboto Regular", 20 * -1)
    )
    
    canvas.create_rectangle(
        10.0,
        251.0,
        630.0,
        377.0,
        fill="#FFE5F2",
        outline=""
    )
    
    canvas.create_text(
        17.0,
        262.0,
        anchor="nw",
        text="Beatmap Name:",
        fill="#2F2F2F",
        font=("Roboto Regular", 20 * -1)
    )

    canvas.create_text(
        18.0,
        302.0,
        anchor="nw",
        text="Beatmap Size:",
        fill="#2F2F2F",
        font=("Roboto Regular", 20 * -1)
    )
    
    canvas.create_text(
        18.0,
        342.0,
        anchor="nw",
        text="Beatmap Download:",
        fill="#2F2F2F",
        font=("Roboto Regular", 20 * -1)
    )
    
    canvas.create_text(
        448.0,
        345.0,
        anchor="nw",
        text="Download Speed:",
        fill="#2F2F2F",
        font=("Roboto Regular", 14 * -1)
    )

    name_text = canvas.create_text(
        197.0,
        262.0,
        anchor="nw",
        text="",
        fill="#2F2F2F",
        font=("Roboto Regular", 20 * -1)
    )
        
    size_text = canvas.create_text(
        197.0,
        302.0,
        anchor="nw",
        text="",
        fill="#2F2F2F",
        font=("Roboto Regular", 20 * -1)
    )
    
    progress_text = canvas.create_text(
        227.0,
        350.0,
        anchor="nw",
        text="",
        fill="#2F2F2F",
        font=("Roboto Regular", 16 * -1)
    )

    speed_text = canvas.create_text(
        573.0,
        350.0,
        anchor="nw",
        text="",
        fill="#2F2F2F",
        font=("Roboto Regular", 12 * -1)
    )

    entry_image_1 = PhotoImage(
        file=resource_path("assets/frame0/entry_1.png"))
    entry_bg_1 = canvas.create_image(
        281.0,
        146.0,
        image=entry_image_1
    )
    id_entry = Entry(
        bd=0,
        textvariable=id_var,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    id_entry.place(
        x=209.0,
        y=136.0,
        width=144.0,
        height=18.0
    )

    entry_image_2 = PhotoImage(
        file=resource_path("assets/frame0/entry_2.png"))
    entry_bg_2 = canvas.create_image(
        337.0,
        186.0,
        image=entry_image_2
    )
    location_entry = Entry(
        bd=0,
        textvariable=location_var,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    location_entry.insert(-1, default_location)
    location_entry.place(
        x=209.0,
        y=176.0,
        width=256.0,
        height=18.0
    )

    button_image_1 = PhotoImage(
        file=resource_path("assets/frame0/button_1.png"))
    button = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: threaded_download(id_var.get(), location_var.get(), callback),
        relief="flat"
    )
    button.place(
        x=513.0,
        y=176.0,
        width=90.0,
        height=23.0
    )
    
    progress = ttk.Progressbar(
        window, 
        orient="horizontal", 
        length=620, 
        mode='determinate'
    )
    progress.place(
        x=10.0,
        y=390.0
    )
    
    # Start the main loop
    window.resizable(width=False, height=False)
    window.mainloop()

def threaded_download(id, location, callback):
    thread = threading.Thread(target=lambda: callback(id, location), daemon=True)
    thread.start()

def disable_button():
    button.config(state="disabled")

def enable_button():
    button.config(state="active")

def info(infotext):
    enable_button()
    infobox = messagebox.showinfo(title="Sucess!", message=infotext)

def warning(warningtext):
    enable_button()
    warningbox = messagebox.showwarning(title="Warning", message=warningtext)
    
def error(errortext, callback):
    enable_button()
    progress['value'] = 0
    errorbox = messagebox.showerror(title="Error!", message=errortext)
    if((errorbox == "ok") & (callback != None)):
        callback()