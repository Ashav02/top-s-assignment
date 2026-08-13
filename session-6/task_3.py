#Remove a playlist from the playlist_prices dictionary using the del statement.
#Print the dictionary after deletion to confirm the change.

playlist_prices = {"90's old songs": 199, "2000's Era": 159,
                   "Kishor Kumar": 249, "Udit Narayan": 249, "Himesh Reshamiya": 249}

del playlist_prices["Kishor Kumar"]


print(playlist_prices)