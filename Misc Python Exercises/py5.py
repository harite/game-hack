from sys import argv
script, input_file = argv

def print_all(f):
    print f.read()
def rewind(f):
    print f.seek(0)
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First, let's print the whole file."
print_all(current_file)

print "Now to rewind to line 0, since that took us to the end."
rewind(current_file)

print "Now to print three lines."

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
