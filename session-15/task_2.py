#Simulate a Zomato-style rating system: ask the user for number of reviews and total stars, then calculate average rating.
#Use try-except to handle invalid (non-numeric) input and print an error message if input is not a number.

try: 
    review = input("Enter number of reviews: ")
    review_1 = int(review)

    total_star = input("Enter total star: ")
    total_star_1 = int(total_star)

    avg_rating = total_star_1 / review_1

    print("Average Rating: ", avg_rating)

except ValueError:
    print("Error: Please enter number only: ")
    