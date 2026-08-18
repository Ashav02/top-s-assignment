#Read the my_playlist.txt file you created and print each song name in uppercase using Python file handling.

file = open("my_playlist.txt", "r")

for song in file:
    print(song.strip().upper())

file.close()