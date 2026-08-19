#Add a method play_preview(self) to your Song class
#that prints 'Playing 30-second preview of [title] by [artist]'. Call this method for your Song object.

class Song:
    def __init__(self, title, singer, duration):
        self.title = title 
        self.singer =singer
        self.duration = duration

    def play_preview(self):
        print(f"playing 30-second preview of {self.title} ft {self.singer}")

song4 = Song("Ek Dil Hai","Kumar Sanu & Alka Yagnik", 503)     
song4.play_preview()