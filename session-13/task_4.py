#Create a recursive function count_likes(posts)


def count_likes(post):
    total = post["likes"]

    if "replies" in post:
        for reply in post["replies"]:
            likes = likes + count_likes(reply)

    return likes

    
post = {"likes": 10, "replies": [{"likes": 5}, {"likes": 3, "replies": [{"likes": 2}]}]}
print(count_likes(post))