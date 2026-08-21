#Add a method play_preview(self) to your Song class
#that prints 'Playing 30-second preview of [title] by [artist]'. Call this method for your Song object.

#Class_1 (Perent)

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play_preview(self):
        print(f"Playing 30-second preview of {self.title} by {self.artist}")

#Object
Track = Song("Ek Dil Hai", "Alka Yagnik & Kumar Sanu")
Track.play_preview()
