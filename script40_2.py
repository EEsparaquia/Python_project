from cx_Freeze import setup, Executable

setup(name='script40', 
	version='0.1', 
	description='Parse stuff',
	executables=[Executable("script40.py")] )


'''
	After doing this you need to run
	from the command line
	$ python script40.py build	
'''