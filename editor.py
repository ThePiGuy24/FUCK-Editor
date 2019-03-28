import tkinter as tk
import time

window = tk.Tk()
window.title("FUCK")
window.iconbitmap("icon.ico")

textbox = tk.Text(window,width=80,height=32)
textbox.grid(column=0,row=0)

def meep():
	textbox.insert("end","\nyou think i added save functionality, think again...")

def about():
	popup = tk.Toplevel()
	popup.title("FUCK")
	tk.Label(popup,text="Fun\nUnusual\nCoding\nKit\n\nLiterally just a really shitty text editor that can't save.\n\n\"Better than DRX\" - Everyone").grid(column=0,row=0)
	tk.Button(popup,text="no",width=16,command=popup.destroy).grid(column=0,row=1)
	try:
		while True:
			popup.update()
			window.update()
			time.sleep(1/60)
	except:
		pass

menubar = tk.Menu(window)
menus = {
	"File": tk.Menu(menubar,tearoff=0),
	"About": tk.Menu(menubar,tearoff=0)
	}
menucontents = {
	"File": {"Meep": meep},
	"About": {"About FUCK": about}
	}
for menu in menus:
	menubar.add_cascade(label=menu,menu=menus[menu])
	for submenu in menucontents[menu]:
		menus[menu].add_command(label=submenu,command=menucontents[menu][submenu])

window.config(menu=menubar)

while True:
	window.update()
	time.sleep(1/60)