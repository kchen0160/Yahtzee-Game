#!/usr/bin/env python3

"""
Functions associated with Yahtzee dice, including dice rolls and scoring
"""
import random
import sys


def roll_dice(dice):
    """
    Replace each value in list of dice with a random number between 1 and 6
    :param dice: a list in which to put dice rolls
    :type dice: list
    :return: the same list with each item set to a new random value between 1 and 6
    :rtype: list
    """
    for i in range(len(dice)):
        dice[i] = random.randint(1, 6)

    return dice


def tally_die_faces(dice):
    """
    Determine the number of 1s, 2s, 3, 4s, 5s, and 6s on  dice faces
    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list of length 5
    :return: a list such that the value at index i is the number of faces equal to i
             (1 <= i <=6) and the value at index 0 is None
    :rtype: list of length 7
    """
    tallies = [None, 0, 0, 0, 0, 0, 0]  # tallies[i] == number of face i occurrences in dice
    for face in dice:
        tallies[face] += 1

    return tallies


def get_chance_score(dice):
    """
    Get the sum of the face values of the dice
    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list
    :return: the sum of the face values of the dice
    :rtype: int
    """

    return sum(dice)   # STUB - TODO


def get_yahtzee_score(dice):
    """
    Determine if the roll is a Yahtzee: 5 of a Kind
    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list
    :return: 50 if the dice show a Yahtzee!, 0 otherwise
    :rtype: int
    """
    if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
        return 50
    return 0


def get_lg_straight_score(dice):
    """
    Determine if the dice roll is a LG Straight
    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list
    :return: 40 if the roll has a sequence of five consecutive numbers, 0 otherwise
    :rtype: int
    """
    if dice[0] != dice[1] != dice[2] != dice[3] != dice[4]:
        return 40
    return 0

def get_sm_straight_score(dice):
    """
    Determine if the dice roll is a SM Straight
    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list
    :return: 30 if the roll has a sequence of four consecutive numbers, 0 otherwise
    :rtype: int
    """
    tallies = tally_die_faces(dice)
    one = tallies[1:5]
    two = tallies[2:6]
    three = tallies[3:7]
    if sum(one) >= 4 and max(one) <= 2 and min(one) == 1:
        return 30
    elif sum(two) >= 4 and max(two) <= 2 and min(two) == 1: 
        return 30
    elif sum(three) >= 4 and max(three) <= 2 and min(three) == 1:
        return 30
    return 0


def get_full_house_score(dice):
    """
    Determine if the dice roll is a full house
    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list
    :return: 25 if any three-of-a-kind and a pair
    :rtype: int
    """
    tallies = tally_die_faces(dice)
    if max(tallies[1:]) == 3 and 2 in tallies:
        return 25
    return 0


def get_4_of_a_kind_score(dice):
    """

    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list
    :return: total of all of the dice if there are 4 of a kind, 0 otherwise
    :rtype: int
    """
    tallies = tally_die_faces(dice)
    if max(tallies[1:]) >= 4:
        return sum(dice)
    return 0


def get_3_of_a_kind_score(dice):
    """
    Compute the maximum score under 3-of-a-kind
    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list
    :return: total of all of the dice if there are 3 of a kind, 0 otherwise
    :rtype: int
    """
    # three_of_a_kind_score([1, 3, 1, 4, 5])  ->  0
    # three_of_a_kind_score([2, 1, 3, 2, 2])  ->  10
    # three_of_a_kind_score([2, 2, 2, 2, 2])  ->  10

    tallies = tally_die_faces(dice)
    if max(tallies[1:]) >= 3:
        return sum(dice)
    return 0


def get_sixes_score(dice):
    """
    Count and add only sixes
    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list
    :return: The sum of dice faces with a 6 on top
    :rtype: int
    """
    return dice.count(6) * 6


def get_fives_score(dice):
    """
    Count and add only fives
    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list
    :return: The sum of dice faces with a 5 on top
    :rtype: int
    """
    return dice.count(5) * 5


def get_fours_score(dice):
    """
    Count and add only fours
    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list
    :return: The sum of dice faces with a 4 on top
    :rtype: int
    """
    return dice.count(4) * 4


def get_threes_score(dice):
    """
    Count and add only threes
    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list
    :return: The sum of dice faces with a 3 on top
    :rtype: int
    """
    return dice.count(3) * 3


def get_twos_score(dice):
    """
    Count and add only twos
    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list
    :return: The sum of dice faces with a 2 on top
    :rtype: int
    """
    return dice.count(2) * 2


def get_aces_score(dice):
    """
    Count and add only aces
    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list
    :return: The sum of dice faces with a 1 on top
    :rtype: int
    """
    return dice.count(1)


SCORING_CATEGORIES = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', '3 of a Kind', '4 of a Kind', 'Full House',
                      'SM Straight', 'LG Straight', 'YAHTZEE', 'Chance']


def evaluate_dice_rolls(dice):
    """
    Determine the scoring possibilities for a roll of five dice
    :param dice: a list of five int values between 1 and 6 representing dice faces
    :type dice: list
    :return: a dictionary whose keys are the items in SCORING_CATEGORIES and whose values are the score in each
             of the categories
    :rtype: dict
    """

    return {'Aces': 0,
            'Twos': 0,
            'Threes': 0,
            'Fours': 0,
            'Fives': 0,
            'Sixes': 0,
            '3 of a Kind': 0,
            '4 of a Kind': 0,
            'Full House': 0,
            'SM Straight': 0,
            'LG Straight': 0,
            'YAHTZEE': 0,
            'Chance': 0
            }   # STUB - TODO


def main():
    """
    Call each of the functions in this module that evaluates a score and display the
    value returned.
    :return: None
    :rtype: None
    """

    if len(sys.argv) == 1:
        # Generate a random roll.
        print('No command line arguments provided so using a random roll')
        dice = roll_dice([1] * 5)
        print(f'                    roll_dice([1] * 5) -> {dice}')
        print()
    elif len(sys.argv) != 6:
        # Some or all command line arguments are missing
        print('Provide exactly five face values on the command line', file=sys.stderr)
        print('Usage: python3 yahtzeedice.py <face1> <face2> <face3> <face4> <face5>', file=sys.stderr)
        exit(1)
    else:
        # Construct a list of five die faces from the command line arguments
        try:
            dice = [int(face) for face in sys.argv[1:]]
        except Exception as e:
            print('Error processing command line arguments.', file=sys.stderr)
            exit(2)

    # Call each of the functions in this module and display the value returned
    for fun in (tally_die_faces, get_chance_score, get_yahtzee_score, get_lg_straight_score,
                get_sm_straight_score, get_full_house_score, get_4_of_a_kind_score,
                get_3_of_a_kind_score, get_sixes_score, get_fives_score, get_fours_score,
                get_threes_score, get_twos_score, get_aces_score):
        print(f'{fun.__name__:>21}({dice}) -> {fun(dice)}')


if __name__ == '__main__':
    main()
