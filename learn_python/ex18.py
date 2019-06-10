# this one is like your script with argv
def print_two(*args):  # def 即“定义”define
    arg1, arg2 = args  # 4个空格
    print("arg1: %r, arg2: %r" % (arg1, arg2))


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):  # 两个空白行
    print("arg1: %r, arg2: %r" % (arg1, arg2))


# this just takes one argument
def print_one(arg1):
    print("arg1: %r" % arg1)


# this one takes no arguments
def print_none():
    print("I got nothing.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
