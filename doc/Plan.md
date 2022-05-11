###Requirements

This program aims to act as a text editing tool that replaces specified words in a given text file with a different word given by the user. User should be able to continue editing their given file in this manner until quitting the program. Options for entering the words to replace and replace with, swapping, printing, and saving will allow the user to make multiple swaps for multiple different words all in the same run of the program while also having the ability to check their progess and save multiple instances of their changes at any given time.

####Program General Goals/Requirements:

	- Program should be able to properly open files and close them
	- Program should take user input from the command line
	- Program should follow the command line format:
		- `$ python [src_dir]/wordSwapper.py [data_dir]/data.txt` 
	- Program should recognize incorrect formatting of command line
	- Program should only replace whole *words* not pieces of words.
		- Ex: when told to replace "no" with "yes" program should recognzie that a word like "nowhere" is not the same as "no" even thought "no" is contained in "nowhere"
	- Program should have simple user interface asking the user for:
		- The word to replace
		- The word to replace the old word with
		- The name of the save to file
	- Program should have simple menu screen that loops until the user decides to quit the wordSwapper program
	- Program should allow user to:
		- print the file to screen to see the progress
		- 


###System Analysis
	
	- User Given Input:
		- filepath: string
		- wordToReplace: string
		- replacementWord: string
		- menuCommand: string
	- Program Output:
		- file: text file


	- Things I'll need to know to complete this:
		- how to open a file
		- how to traverse a file
		- how to parse strings
		- how to edit lists
		- how to check if a file can be opened before actually opening it
	

###Design

####Driver.py

```python 

	#checks the input from the command line is valid and responds accordingly

if sys.argv[1] is not valid (ei it's not able to be opened)
	return a usage message
	quit
if too many args
	return a usage message
	quit
else if sys.argv[1] is valid
	open file and save to fileobj
	create a menu obj and populate with commands
		#command for entering new word to replace
		#command for entering new replacement word
		#command for printing current progress 
		#command for saving to specified file
		#command for quitting
	start menu loop until quit is entered	

```


####Menu.py

```python 

	#a menu object has the ability to have a specified title, add commands to it's list, print itself, and possibly take commands?

class Menu():
	def __init__(self, title)
		self.title = title
		self.commands = new dict
	
	def addCommand(self, command, description)
		add a new command to the commands dictionary
		command is the key
		description is the value
	
	def printMenu(self)
		for each item in the dictionary
		print it in the format "key : description"
		menu should have some sort of styling to it
	
	def isCommand(self, command)
		if command is one of the commands dictionary keys 
			return true
		else 
			return false 

```


####Replace.py

```python




```



###Implementation

###Testing

###Deployment
