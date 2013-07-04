from sys import argv

script, filename = argv

print "Oh, a file! Let's open it and see what it says!"

print "Opening..."
target = open(filename,'r')

print "Oh, interesting. Here, take a look!"
print target.read()
