formatter = "%r %r %s %s"

print(formatter % (1, 2, 3, 4))  # %前后要加空格  ，后要加空格
print(formatter % ('one', 'two', 'three', 'four'))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I had goodnight."
))