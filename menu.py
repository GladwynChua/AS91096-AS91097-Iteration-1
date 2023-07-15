
#Import the required libraries
from tkinter import *
import tkinter as tk
import sys
from tkinter import messagebox

def credits_message():
   messagebox.showinfo("Price Comparison: Botany Supermarkets",message="This code was developed by Gladwyn Chua ©. " "Thanks to New World, Countdown and Pak 'n Save for providing me with the prices to compare from.                 Last Price Updated 13/07/23")

def quit():
   messagebox.showinfo("Price Comparison: Botany Supermarkets",message="Hope to see you again soon!")
   sys.exit()

def menu_popup(event):
   # display the popup menu
   try:
      popup.tk_popup(event.x_root, event.y_root, 0)
   finally:
      #Release the grab
      popup.grab_release()  

   
#Create an instance of Tkinter frame
win = Tk()

#Set the geometry of the Tkinter library
win.attributes("-fullscreen", True)


# Create the banner
banner_frame = tk.Frame(win, bg="#2F4F4F")
banner_frame.pack(fill="x")

banner_label = tk.Label(banner_frame, text="Price Comparison: Botany Supermarkets", font=("Arial", 35, "bold"), fg="white", bg="#2F4F4F")
banner_label.pack(pady=10)


#Add Menu
popup = Menu(win, tearoff=0) 

start = tk.Button(win, text="Start", bg="#2F4F4F", command=win.destroy, width = 20,  fg="white", font=('Ariel', 45,))
start.place(relx=0.25, rely=0.32)

recognition = tk.Button(win, text="Credit", bg="#2F4F4F", command=credits_message, width = 20,  fg="white", font=('Ariel', 45,))
recognition.place(relx=0.25, rely=0.52)


exit = tk.Button(win, text="Quit", bg="#2F4F4F", command=quit, width = 20, fg="white",font=('Ariel', 45))
exit.place(relx=0.25, rely=0.72)

mainloop()





