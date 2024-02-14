from itertools import product


def calculate_probabilities(dice):
    """
    Calculate the probabilities of obtaining each sum when rolling the dice.
    """
    probabilities = [0] * (len(dice) * 6 + 1)
    for outcome in product(*[dice] * len(dice)):
        probabilities[sum(outcome)] += 1
    total_outcomes = sum(probabilities)
    probabilities = [count / total_outcomes for count in probabilities]
    return probabilities


def undoom_dice(Die_A, Die_B):
    """
    Transform the dice to fulfill the conditions imposed by Loki.
    """
    # Calculate current probabilities for both dice
    probabilities_A = calculate_probabilities(Die_A)
    probabilities_B = calculate_probabilities(Die_B)

    # Calculate the minimum number of spots required to preserve probabilities
    min_spots = max(max(Die_A), max(Die_B))

    # Modify Die A to have at most 4 spots per face
    New_Die_A = [min(spots, 4) for spots in Die_A]

    # New_Die_B remains the same as Die_B
    New_Die_B = Die_B

    return New_Die_A, New_Die_B


# Input
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

# Output
New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)



