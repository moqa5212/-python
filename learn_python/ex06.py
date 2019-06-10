x = 'there are %d type of people.' % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print (x)
print (y)

print ('I sad: %r' % x) # %r 给字符串加引号
print ("I also sad: %s" % y) # %s 不加引号

hilarious = False
joke_evaluation = "Isn't that joke so fanny?! %r"

print (joke_evaluation % hilarious)

w = "That is the left side of..."
e = "a string with a right side."

print (w + e)
