from sys import argv
script, from_file, to_file = argv
#See if you can bring the code below down to one line.
indata = open(from_file,'r').read() #Opens and reads the file
output = open(to_file,'w').write(indata) #Writes indata to the output file
