class Song(object):
    def __init__(self, lyrics):  # 一边两个下划线（_ __)
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_birthday = Song(["Happy birthday to you",
                       "I don't want to get sued",
                       "So I'll stop right there"])

bulls_on_parade = Song(["They birthday to you",
                        "I don't want to sued",
                        "So I'll stop right there"])

happy_birthday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

print(type(happy_birthday))


