from sys import argv

script, filename = argv

print "We're going to erase %r."  % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w+')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

lines = ('line1', 'line2', 'limne3')
target.write(lines)


print "And finally, we close it."
target.close()

target_read = open(filename)

print "What you wrote is.. "
print target_read.read()

print "And finally, we close it."
target_read.close()

