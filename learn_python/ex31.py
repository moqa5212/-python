print("You enter  dark room with two doors. Do you though door #1 or door #2?")

door = input(">")

if door == "1":
    print("There is a giant bear here eating a cheese cake. What do you do?")
    print("1\.Take the cake.")
    print("2\.Scram at the bear.")

    bear = input(">")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your left off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print("You star into the endless abyss at Zed's retina.")
    print("1\.Blueberries.")
    print("2\.Yellow jacket clothespins.")
    print("3\.Understanding revolvers yelling melodies.")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print("Your body survived by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
