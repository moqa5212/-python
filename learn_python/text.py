# 读取文件
"""
text = open("cool.txt", "w")
text.write("hello,world!")
text.write("hi,bye!")
"""
"""
c = 2
print("a", c, "b")
"""
"""
# a = b = c = 1
a, b, c = 1, 2, "john"
print(a, b, c)
"""
"""
a = list(range(5))

a.reverse()

print(a)

"""
"""
print("*" * 6, "\t", "*" * 6)
print("*" * 15)
"""
"""
a = [1, 2, 3]
b = [str(i) for i in a]

print(b)
"""
"""
a = ""
b = "jack"
print(a + b)
"""
"""
print(hash('a') % 345)
"""
"""
import urllib.request
url="http://learncodethehardway.org/words.txt"
get=urllib.request.urlopen(url).read()
print(get)
"""
"""
import random
PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

from urllib.request import urlopen
snippets = PHRASES.keys()
print(type(snippets))
random.shuffle(list(snippets))
print(list(snippets))
WORDS = []
WORD_URL = "http://learncodethehardway.org/words.txt"
i = 0
for word in urlopen(WORD_URL).readlines():
    print(word)
    a = word.strip().decode('ascii')
    print(a)
    WORDS.append(a)
    print(WORDS)
    i = i +1
print(i)
for i in snippets:
    print(type(i))
    print(i.count('***'))
"""
"""
a = []
b = "kill"
c = 2
print(type(b))
a.append(b)
d = a * 5
print(d)
f = "alkilldooskillds".replace(b, "help", 1)
print(f)
"""
"""
import sys

print(sys.argv)
print(len(sys.argv))
print(sys.argv[1])
"""

import requests
from bs4 import BeautifulSoup

r = requests.get(url="https://www.python.org/events/python-events/")
print(r.url)
print('*' * 15)

print(r.content)
print('*' * 15)

soup = BeautifulSoup(r.content, "html.parser")
print(soup)
print('*' * 165)

menu_tag = soup.find_all(class_="uk-nav uk-nav-side")
print(menu_tag)


