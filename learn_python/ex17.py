from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do this two on one line, how?
in_file = open(from_file)
data = in_file.read()
# data = open(from_file).read()

print("The input file is %d bytes long" % len(data))

print("Does the output file exist? %r" % exists(to_file))
print("Really, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(data)

print("Alright, all done.")

out_file.close()
in_file.close()
