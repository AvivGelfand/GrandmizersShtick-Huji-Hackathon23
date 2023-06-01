import tkinter as tk
from tkinter import ttk
from threading import Thread
from ttkthemes import ThemedStyle
import subprocess


def break_run():
    """
    # Function to be executed when the "Break Run" button is clicked, stop the python
    """
    global stop_flag
    stop_flag = True
    subprocess.call("taskkill /f /im python.exe", shell=True)


def appify():
    """
    # Function to be executed when the "Main" button is clicked - run the main_process_voices
    """
    global stop_flag
    stop_flag = False
    process = subprocess.Popen(["python", "main_process_voices.py"])
    process.wait()


def run_appify():
    """
    # Function to start the appify function in a new thread
    """
    Thread(target=appify).start()


def open_gui():
    """
    # Function to open the GUI window
    """
    # Create the main window
    window = tk.Tk()
    window.title("Ny Grandmizer Guard")

    # Set window dimensions and position
    window_width = 500
    window_height = 300
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Apply a themed style
    style = ThemedStyle(window)
    style.set_theme("radiance")  # You can try different themes: "arc", "clearlooks", etc.

    # Create a headline label
    headline_label = ttk.Label(window, text="Grandmizer Keeper", font=("Calibry", 16, "bold"))
    headline_label.pack(pady=20)

    # Create a frame to hold the buttons
    button_frame = ttk.Frame(window)
    button_frame.pack()

    # Create the "Main" button
    main_button = ttk.Button(
        button_frame,
        text="I'm leaving home, turn on sound",
        command=run_appify,
        width=35
    )
    main_button.pack(pady=10)

    # Create the "Break Run" button
    break_button = ttk.Button(
        button_frame,
        text="I'm back, turn off sound",
        command=break_run,
        width=35
    )
    break_button.pack(pady=10)

    # Create a shared variable to control the main function
    stop_flag = False

    # Run the event loop
    window.mainloop()

open_gui()

