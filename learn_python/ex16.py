from sys import argv

script, filename = argv

print("We are going to erase %r." % filename)
print("If you don't want that, hit CTRL-C(^C).")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()  # clear all the txt

print("Now I'm going to ask you three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
"""
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""
target.write("%s\n%s\n%s\n" % (line1, line2, line3))
print("And finally, we close it.")
target.close()




