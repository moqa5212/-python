print("How old are you?")
age = input()  # 整合了python2.x中的input()和raw_input()
print("How tall are you?")
height = input()
print("How much do you weight?")
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (
    age, height, weight))
# 尽量让每行代码小于80