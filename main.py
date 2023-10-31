import tkinter as tk # GUI
from tkinter import filedialog # File Picking
import subprocess # to run external commands
import pyudev # device list

# Define your color scheme
background_color = "#333"  # Dark gray
text_color = "#FFF"  # White
button_color = "#007ACC"  # Blue
button_text_color = "#FFF"  # White

def select_iso():
    initial_dir = '~/Downloads'  # Specify the initial directory
    file_path = filedialog.askopenfilename(initialdir=initial_dir, filetypes=[("ISO files", "*.iso")])
    iso_entry.delete(0, tk.END)
    iso_entry.insert(0, file_path)

def list_drives():
    drive_list.delete(0, tk.END)
    context = pyudev.Context()
    for device in context.list_devices(subsystem='block'):
        drive_list.insert(tk.END, f"{device.device_node} - {device.device_type}")

def select_drive():
    selected_drive = drive_list.get(tk.ACTIVE).split()[0]
    drive_entry.delete(0, tk.END)
    drive_entry.insert(0, selected_drive)

def burn_iso():
    iso_path = iso_entry.get()
    drive_path = drive_entry.get()

    if not iso_path or not drive_path:
        return

    try:
        command = f"sudo -S dd if='{iso_path}' of='{drive_path}' bs=4M"
        subprocess.run(command, shell=True)
        result_label.config(text="ISO Burned Successfully!", fg="green")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}", fg="red")

# Create the main window
root = tk.Tk()
root.title("ISO Burner")

# Configure the background color
root.configure(bg=background_color)

# Create and place widgets with color theming and increased button spacing
iso_label = tk.Label(root, text="Select ISO Image:", bg=background_color, fg=text_color)
iso_label.pack(pady=5)  # Added spacing between label and entry

iso_entry = tk.Entry(root, width=40, bg=background_color, fg=text_color)
iso_entry.pack()

iso_button = tk.Button(root, text="Browse", command=select_iso, bg=button_color, fg=button_text_color)
iso_button.pack(pady=5)  # Added spacing between buttons

drive_label = tk.Label(root, text="Select Target Drive:", bg=background_color, fg=text_color)
drive_label.pack(pady=5)  # Added spacing between label and listbox

drive_list = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, bg=background_color, fg=text_color)
drive_list.pack()

list_button = tk.Button(root, text="List Drives", command=list_drives, bg=button_color, fg=button_text_color)
list_button.pack(pady=5)  # Added spacing between buttons

drive_entry = tk.Entry(root, width=40, bg=background_color, fg=text_color)
drive_entry.pack()

drive_button = tk.Button(root, text="Select from List", command=select_drive, bg=button_color, fg=button_text_color)
drive_button.pack(pady=5)  # Added spacing between buttons

burn_button = tk.Button(root, text="Burn ISO", command=burn_iso, bg=button_color, fg=button_text_color)
burn_button.pack(pady=5)  # Added spacing between buttons

result_label = tk.Label(root, text="", bg=background_color, fg=text_color)
result_label.pack()

# Start the GUI event loop
root.mainloop()