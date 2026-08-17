#Given a list of cricket scores [45, 78, 102, 34, 67, 89],
#use a while loop to print each score until you reach a score above 100, then stop printing.


cricket_scores = [45, 78, 102, 34, 67, 89]

index = 0
scores = len(cricket_scores)

while index <scores:
    scores_1 = cricket_scores[index]

    if scores_1 > 100:
        break
    print(scores_1)
    index += 1

