import tkinter as tk
from tkinter import messagebox


def save_settings():
    # Placeholder function to save settings
    messagebox.showinfo("Settings", "Settings saved!")


def open_about():
    # Placeholder function to open about dialog
    messagebox.showinfo("About", "This is a simple Tkinter application.")


def open_settings_window():
    settings_window = tk.Toplevel(window)
    settings_window.title("Settings Window")

    # Add your widgets and settings for the settings window here


# Create the main Tkinter window
window = tk.Tk()
window.title("Settings")

# Create the menu bar
menu_bar = tk.Menu(window)

# Create the file menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save Settings", command=save_settings)
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create the help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=open_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Create the settings menu
settings_menu = tk.Menu(menu_bar, tearoff=0)
settings_menu.add_command(label="Settings", command=open_settings_window)
menu_bar.add_cascade(label="Settings", menu=settings_menu)

# Configure the window to use the menu bar
window.config(menu=menu_bar)

# Add your widgets and settings for the main window here

# Start the Tkinter event loop
window.mainloop()
