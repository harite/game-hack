def add(a,b):
    print "ADDING %d and %d" % (a,b)
    return a + b
def subtract(a,b):
    print "SUBTRACTING %d from %d" % (a,b)
    return a - b
def multiply(a,b):
    print "MULTIPLYING %d by %d" % (a,b)
    return a*b
def divide(a,b):
    print "DIVIDING %d by %d" % (a,b)
    return a/b

print "Let's do some math with functions!"
age = add(20, 5)
height = subtract(200, 20)
weight = multiply(60, 2)
iq = divide (600, 3)

print "Age: %d, Height: %d, Weight: %d, iq: %d" % (age, height, weight, iq)

#Ha ha puzzle time

print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

next = divide(weight, multiply(iq, add(age, subtract(height, 4))))
print "that makes", next, "!"
