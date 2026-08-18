#Build a recursive function sum_playlist_durations(durations)
#that takes a list of song durations (in seconds)
#and returns the total duration, similar to how Spotify totals a playlist.

def sum_playlist_durations(durations):
    if len(durations) == 0:
        return 0
    return durations[0] + sum_playlist_durations(durations[1:])

play_time = [119,128,255,150,140]
print(sum_playlist_durations(play_time)) 

