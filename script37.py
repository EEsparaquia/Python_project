#! Python3

# Programming Tutorial
# Tkinter module making windows Module 4
# Make a menu

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


		# Make the menu
		menu = Menu(self.master)
		self.master.config(menu=menu)

		# Add FILE button to the menu and in the button some elements:
		file = Menu(menu)
		file.add_command(label='Close', command=self.client_exit)
		file.add_command(label='Exit', command=self.client_exit)
		menu.add_cascade(label='File', menu=file)

		# Add EDIT button to the menu and in the button some elements:
		edit = Menu(menu)
		edit.add_command(label='Undo', command=self.client_exit)
		menu.add_cascade(label='Edit', menu=edit)
        

	def client_exit(self):
		exit()

root = Tk()
root.geometry("400x300")
app = Window(root)

root.mainloop()