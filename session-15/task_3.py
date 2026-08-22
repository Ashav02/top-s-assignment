#Create a function get_playlist_duration(songs) that takes a list of song durations (in seconds) and returns the total duration in minutes.
#Raise a custom exception InvalidDurationError if any duration in the list is negative.

class InvalidDurationError(Exception):
    pass

def get_playlist_duration(songs):
    total_second = 0

    for duration in songs:
        if duration < 0:
            raise InvalidDurationError ("Song duration can't be nagitive.")
        total_second += duration
    return total_second / 60

songs = [245,200,220,325]

try:
    duration = get_playlist_duration(songs)
    print("Total playlist duration:", duration, "minutes")

except InvalidDurationError as e:
    print("Error:", e)