import requests
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

# Window in full screen mode
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")


def downloadImage(url, location, filename):
    try:
        response = requests.get(url)
        with open(location + "\\" + filename, "wb") as picture:
            picture.write(response.content)
        messagebox.showinfo("Message Box", "Downloaded")
    except:
        messagebox.showinfo("Message Box", "First enter all entries correctly")


background_image = tk.PhotoImage(file="mountains5.png")
background_label = tk.Label(window, image=background_image)
background_label.pack()

frame = tk.Frame(window, bg="#d2d3d4", bd=5)
frame.place(relx=0.3, rely=0.17,
            relheight=0.6, relwidth=0.4)

url_label = tk.Label(frame, text="URL:", bg="#d2d3d4",
                     font=("Microsoft Himalaya", 20))
url_label.place(relx=0.07, rely=0.1,
                relheight=0.1, relwidth=0.15)

url_entry = tk.Entry(frame, font=("System", 17))
url_entry.place(relx=0.25, rely=0.1,
                relheight=0.1, relwidth=0.65)

location_label = tk.Label(frame, text="Location:", bg="#d2d3d4",
                          font=("Microsoft Himalaya", 20))
location_label.place(relx=0.07, rely=0.25,
                     relheight=0.1, relwidth=0.15)

location_entry = tk.Entry(frame, font=("System", 17))
location_entry.place(relx=0.25, rely=0.25,
                     relheight=0.1, relwidth=0.65)

filename_label = tk.Label(frame, text="FileName:", bg="#d2d3d4",
                          font=("Microsoft Himalaya", 20))
filename_label.place(relx=0.07, rely=0.4,
                     relheight=0.1, relwidth=0.15)

fileName_entry = tk.Entry(frame, font=("System", 17))
fileName_entry.place(relx=0.25, rely=0.4,
                     relheight=0.1, relwidth=0.65)

button = tk.Button(frame, text="Download",
                   font=("System", 17),
                   command=lambda: downloadImage(url_entry.get(), location_entry.get(), fileName_entry.get()))
button.place(relx=0.35, rely=0.6, relheight=0.1, relwidth=0.3)


window.mainloop()
