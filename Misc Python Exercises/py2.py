from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you want this, hit RETURN."
print "Otherwise, hit ctrl-c."

raw_input("?")
newline = "\n"

print "Opening the file..."
target = open(filename,'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now, I'm going to ask you for three lines."

line1 = raw_input('> ')
line2 = raw_input('> ')
line3 = raw_input('> ')
writecontent = line1 + newline + line2 + newline + line3 + newline

print "Now to write them to a file."

target.write(writecontent)

print "and finally, we close it."
target.close()
