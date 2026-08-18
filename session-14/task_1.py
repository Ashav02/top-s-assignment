#called my_playlist.txt

songs = ["Hanuman Chalisha", "Rangtali-2", "Shiv-Stuti", "Kalyani", "Raat bhar"]

file = open("my_playlist.txt", "w")

for i in songs:
    file.write(i + "\n")

file.close()