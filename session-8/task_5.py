#Write a for loop that goes through a list of Instagram follower counts [120, 1500, 23000, 800, 45000] and prints 'Micro', 'Influencer', or 'Celebrity' for each,
#based on the following: Micro (<1000), Influencer (1000-10000), Celebrity (>10000).

follower_counts = [120, 1500, 23000, 800, 45000]

for count in follower_counts:
    if count < 1000:
        print("Micro")
    elif count <= 10000:
        print("Infulencer")
    else:
        print("Celebrity")
