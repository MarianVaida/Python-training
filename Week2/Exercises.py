import sys
# Conditionals
# Define a main() function that computes the maximum (z) of a and b.
def main():
  a = 1
  b = 2
  c = 3
  if a < b:
    z = b
    print "z este: %d" % (z)
  
# Empty clause  
  if c < b:
    pass #do nothing
  else:
    z = c
    print "z este: %d" % (z)
    
# Boolean expression using or, and, not
  if b>=a and b<=c:
    print "b is between a and c"
  
  if not (b<a or b> c):
    print "b is still between a and c"
    
# Multiple case with elif
    a = '-'
    if a == '+':
        op = 'PLUS'
    elif a == '-':
        op = 'MINUS'
    elif a == '*':
        op = 'MULTIPLY'
    else:
        raise RuntimeError, "Unknown operator"
    print "op is: %s" % op
    
# Boolean values True and False
    if len(sys.argv) >= 2:
        c = sys.argv[1]
    if c in '0123456789':
        isdigit= True
    else:
        isdigit = False
    print isdigit

#File Input and Output
#Read file contents

'''f = open("foo.txt")     #Returns a file object
line = f.readline()     #Invokes readine() method on file
while line:
        print line,     #trailing ',' omits newline character
        line = f.readline()
f.close()
'''
#File reading shorter alternative
for line in open("foo.txt"):
    print line,
    
# Write to a file
    principal = 1000
    rate = 0.05
    numyears = 5
    year = 1
    f = open("out.txt","w")
    while year <= numyears:
        principal = principal*(1+rate)
        #print >> f, "%3d   %0.2f" % (year,principal)
        f.write("%3d   %0.2f\n" % (year,principal))
        year += 1
    f.close()
    
#Read and write from/to interpreter
'''sys.stdout.write("Enter your name:
name = sys.stdin.readline()'''
'''name = raw_input("Enter your name: ")
print "Input name is: %s" % name'''

#Strings
a = "Hello World"
b = 'Python is groovy'
c = """What is footnote 5?"""
print '''Content-typ: text/html

<h1> Hello Wolrd </h1>
'''
d = a[4]
print "4th elem of a is: %s" % d

# Substring extraction
c = a[:5]
print c
d = a[6:]
print d
e = a[3:8]
print e

# Concatenate strings
g = a + " This is a test"
print g
x = 5
y = 2
s = "The value of x is " + str(x)
print s
#s = "The value of y is " + repr(y)
s = "The value of y is " + `y`
print s

#Lists
names = ["Dave", "Mark", "Ann", "Phil"]
print names
a = names[2]    #returns the third item of the list
print "third item is: %s" % a
names[0] = "Jeff"   #changes the first item to "Jeff"
print names
names.append("Kate")
print "Add Kate at the end: %s" % names
names.insert(2, "Sydney")
print "Insert Sydney as 3rd: %s" % names
b = names[0:2]
print "Extract first 2 items: %s" % b
c = names[2:]
print "Extract item starting with 3rd: %s" % c
names[1] = 'Jeff'
print "Replace 2nd item with Jeff: %s" % names
names[0:2] = ['Dave', 'Mark', 'Jeff']
print "Replace first two items: %s" % names

#Concatenate lists
a = [1,2,3]+[4,5]
print a

a = [1, 'Dave',3.14, ['Mark',7,9,[100,101]],10]
print "a = %s" % a
print "a[1] is: %s" % a[1]
print "a[3][2] is: %s" % a[3][2]
print "a[3][3][1] is: %s" % a[3][3][1] 

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
