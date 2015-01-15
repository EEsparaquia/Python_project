#! Python3

# Programming Tutorial
# Tkinter module making windows Module 3
# Adding functions to buttons

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
		# We add a third parameter called "command"
		# and create the self.client_exit
		quitButton = Button(self, text="Quit", command=self.client_exit)

		quitButton.place(x=0, y=0)

	def client_exit(self):

		exit()

root = Tk()
root.geometry("400x300")
app = Window(root)

root.mainloop()