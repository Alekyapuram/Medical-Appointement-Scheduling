import tkinter as tk
from tkinter import *
import socket
from tkinter import messagebox

def update():
    messagebox.showinfo("Info", "SUCCESSFULLY STARTED THE SERVER")
    FORMAT = 'utf-8'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((socket.gethostname(), 22222))
    client, addr = sock.recvfrom(1024)
    
    with open("a.txt", "r") as f:
        readfile = f.readlines()
    
    client = client.decode(FORMAT)
    y = client.split()
    flag = "0"
    for line in readfile:
        if y[0] in line:
            s = line.split()
            if s[1] == y[1]:
                flag = "1"
                sock.sendto(flag.encode(FORMAT), addr)
                break
    
    if flag != "1":
        sock.sendto(flag.encode(FORMAT), addr)
        with open("a.txt", "a") as f:
            f.write(" ".join(y) + "\n")

def show():
    with open("a.txt", "r") as m:
        con = m.read()
    
    tb = tk.Text(root, height=10, width=35)
    tb.insert(1.0, con)
    tb.place(x=9, y=40)

root = tk.Tk()
root.title("SERVER DATABASE")
root.geometry("600x600")
root.config(bg="#189AB4")
root.resizable(False, False)

Label(root, text="TODAYS APPOINTMENTS", font=("montserrat", 28, 'bold'), bg="#f4f5f6").place(x=20, y=5)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((socket.gethostname(), 22222))
host = sock.getsockname()
sock.close()

Label(root, text=f'ID: {host}', bg="#f4f5f4").place(x=100, y=500)

d = Button(root, text="START", font=9, bg="WHITE", command=update)
d1 = Button(root, text="SHOW", font=9, bg="WHITE", command=show)

d.place(x=20, y=400)
d1.place(x=400, y=400)

root.mainloop()
