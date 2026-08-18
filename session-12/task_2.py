#Given a list of song titles from Spotify with extra spaces and inconsistent casing, use map() and a lambda function to clean each title so that it is stripped of spaces and converted to title case
#(e.g., ' shape OF you ' → 'Shape Of You').

songs = [' shape OF you' , ' love me like a do ' , ' wake me up ']

clean_songs = list(map(lambda x:x.strip().title(),songs))
print(clean_songs)
