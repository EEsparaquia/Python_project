#! Python3

# Programming Tutorial
# Tkinter module making windows Module 2
# Adding buttons

print('''
        #####################
        #                   #
        #  Starting Python3 #
        #      Scripts.     #
        #  It's an exciting #
        # time to be alive  #
        #                   # 
        #####################

''')

from tkinter import *

class Window(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)

		self.master = master

		self.init_window()

	# initialize buttons

	def init_window(self):
		
		self.master.title("GUI") # Title of our window 

		self.pack(fill=BOTH, expand=1)

		quitButton = Button(self, text="Quit")

		quitButton.place(x=0, y=0) 


root = Tk()
root.geometry("400x300")
app = Window(root)

root.mainloop()