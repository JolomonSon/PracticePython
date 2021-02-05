import tkinter as tk    
from tkinter import filedialog,Text
import os

root = tk.Tk()
apps = []
def addApps():
    fileName = filedialog.askopenfilename(initialdir='/Pictures',title="Select File",filetypes=(('applications','*.exe'),('all files','*.*')))
    apps.append(fileName)
    for app in apps:
        label = tk.Label(frame, text=app, bg='grey')
    label.pack()
    
def runApps():
    for app in apps:
        os.startfile(app)
        
canvas = tk.Canvas(root, height=600, width = 500, bg = "grey")
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)

openFile = tk.Button(root, text="Open File", bg="grey",border="1px",padx=12,pady=5, command=addApps)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", bg="green",border="2px",padx=10,pady=5, command=runApps)
runApps.pack()


root.mainloop()
