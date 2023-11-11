import tkinter as tk
import time
import pyperclip

def getTimeNow():
    # Get current time
    current_time = time.localtime()

    # Format the time as per your requirement
    formatted_time = time.strftime("%Y_%m_%d_%H-%M-%S", current_time)

    # Copy to clipboard
    pyperclip.copy(formatted_time)

    # Change button color and disable after being pressed
    button.config(state=tk.DISABLED, bg='#404040')  # Dark grey color

    # After 5 seconds, revert button color and enable
    root.after(5000, lambda: button.config(state=tk.NORMAL, bg='SystemButtonFace'))

# Create the main window
root = tk.Tk()
root.title("Time Generator")

# Increase default size by 15 pixels in all directions
root.geometry("330x120")

# Create a button
button = tk.Button(root, text="Generate Time", command=getTimeNow)
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
