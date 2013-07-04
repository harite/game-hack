from sys import argv #Imports the modules to allow the file to take arguments

script, filename = argv #defines the argument as a string
prompt = "dicks:" #sets the prompt

txt = open(filename) #Opens the file specified in the argument via line 3
print "Here's your file %r:" % filename #Statement, %r to substitute instead of hardcoded.
print txt.read() #Displays the text in the file
txt.close() #closes the file we no longer need.

print "I'll also ask you to type it again." #Print statement.
file_again = raw_input(prompt) #Asks for another filename

txt_again = open(file_again) #Defines the file as a string (Note not the contents)

print txt_again.read()  #reads and prints the contents of the file.
txt_again.close()
