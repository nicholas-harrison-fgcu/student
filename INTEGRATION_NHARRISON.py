# Nicholas Harrison.
# Dungeons and Dragons 5th Edition Character Generator.
# Imports math and random.
import math
import random


# Combines user progression and line spacing in one function.
def continue_key_press():
    input("Press any key to continue: ")
    print(" ")


# Function for player early summary to be called multiple times. Has sep.
def get_early_summary(name_player, race_select, class_select):
    a = "Your summary so far."
    print("Your name's ", name_player, ", you're fairly certain of this.", sep='')
    if race_select == 1:
        print("You are a Half-Orc. How scary.")
    elif race_select == 2:
        print("You are a Human. How tame.")
    else:
        print("You are a Halfling. How tiny.")
    if class_select == 1:
        print("Fighter. Primary: strength. Saves: strength, constitution.")
    elif class_select == 2:
        print("Rogue. Primary: dexterity. Saves: dexterity, intelligence.")
    else:
        print("Wizard. Primary: intelligence. Saves: intelligence, wisdom.")
    return a


# Function for a dice roll. Has range, for, and in to show four rolls.
# Accepts user input later in the program and returns their rolls.
# Fixed with NUM_TIMES for good coding practice.
# Can take this further for general dice roll if I replace range with vars
# for other dice.
def roll_six_side_die_four_times(roll):
    NUM_TIMES = 4
    dice_rolls = []
    if roll == 1:
        for a in range(NUM_TIMES):
            n = random.randint(1, 6)
            dice_rolls.append(n)
    else:
        print("Not rolling.")
    return dice_rolls


def main():
    # Intro and input test. Starts with simple print functions.
    continue_key_press()
    print("Welcome!\nThis is a Dungeons & Dragons character sheet generator.")
    print("This is the second version.")
    continue_key_press()
    print("This program assumes basic knowledge of Dungeons & Dragons.")
    print("Your character creation process is interactive.")
    # First input that is not in a new function.
    answer_any = input("Try it out. Type anything here: ")
    # This is how I will add line spaces without the function.
    print(" ")
    # Concatenate a string.
    print("Wait. You said " + answer_any + "? " + "I'm sure that won't matter.")
    continue_key_press()
    # The below is designed to catch users entering decimals with float.
    # Uses math.floor to give input without decimals, rounded down.
    # It will also guide them to entering 1 the program can progress.
    # Wanted to make my own range/try block for strings. Couldn't do it.
    # I keep trying to use the code from 101computing.net but
    # it keeps breaking the rest of the program for some reason!
    # So, this thing crashes if you put strings in still...
    # I will figure it out later.
    answer_start = float(input("Are you ready? 1 = Yes, 2 = No: "))
    answer_start = math.floor(answer_start)
    # While loop to catch bad input.
    # Relational operators for less/greater than.
    # Boolean operator or.
    while answer_start < 1 or answer_start > 2:
        answer_start = float(input("You have to answer with 1 or 2: "))
        answer_start = math.floor(answer_start)
    # If-else statement for user input of 1 or 2(else).
    # Relational operator for equal.
    if answer_start == 1:
        print(" ")
        print("You are in a dim tavern.\nA cloaked figure turns to you.")
    else:
        answer_start = float(input("You feel compelled to enter 1: "))
        answer_start = math.floor(answer_start)
        # Relational operator for not equal.
        while answer_start != 1:
            answer_start = float(input("You have to answer with 1: "))
            answer_start = math.floor(answer_start)
        else:
            print(" ")
            print("You are in a dim tavern.\nA cloaked figure turns to you.")
    continue_key_press()
    # Naming process.
    print("The cloaked figure has a quill and parchment.\nIt asks...")
    name_player = input("'What should I call you?' Write your name down here: ")
    print(" ")
    print("'Ah,", name_player, "- sounds like an adventurer to me.'")
    answer_name = float(input("Is this your name? 1 = Yes, 2 = No: "))
    answer_name = math.floor(answer_name)
    # Simpler version of the while loop catch from earlier.
    while answer_name == 2:
        name_player = input("'What should I call you?' Write your name: ")
        print(" ")
        print("'Ah,", name_player, "- sounds like an adventurer to me.'")
        answer_name = int(input("Happy with your name? 1 = Yes, 2 = No: "))
    else:
        print(" ")
        print("The cloaked figure says, 'Very well...'")
        continue_key_press()
    print("The cloaked figure takes a closer look at you.\n'What are you?'")
    print("The figure holds a mirror up and you see...")
    continue_key_press()
    print("Half-Orc? Strong.\nHumans, average skills.\nHalflings? Sneaky.")
    print(" ")
    print("Select a race.")
    race_select = float(input("1 = Half-Orc, 2 = Human, 3 = Halfling: "))
    race_select = math.floor(race_select)
    # Catches incorrect input.
    while race_select < 1 or race_select > 3:
        print(" ")
        print("You didn't pick 1, 2, or 3.")
        race_select = float(input("1 = Half-Orc, 2 = Human, 3 = Halfling: "))
        race_select = math.floor(race_select)
    # Nested if-elif-else with trailing else if they do pick correct inputs.
    else:
        if race_select == 1:
            print(" ")
            print("Half-Orc. Strength increases by 2, constitution by 1.")
        elif race_select == 2:
            print(" ")
            print("Human. All ability scores increase by 1.")
        else:
            print(" ")
            print("Halfling. Your dexterity increases by 2.")
    continue_key_press()
    if race_select == 1:
        print("'Aha, I know a half-orc when I see one.'")
    elif race_select == 2:
        print("'Oh, a human? How... interesting?'")
    else:
        print("'A halfling! I barely saw you down there...'")
    continue_key_press()
    print("'Now,' it says, 'I will chant my magic word to find your class.")
    continue_key_press()
    # Multiply the input string by 10 for comedy's sake.
    print(answer_any * 10)
    continue_key_press()
    # Class selection.
    print("That makes sense. You are a...")
    print(" ")
    print("Fighters are good with weapons.\nRogues are sneaky.\nWizard? Magic.")
    print("NOTE: primary ability is what you're good at. Saves... save you.")
    print(" ")
    class_select = float(input("1 = Fighter, 2 = Rogue, 3 = Mage: "))
    class_select = math.floor(class_select)
    while class_select < 1 or class_select > 3:
        print(" ")
        print("Pick 1, 2, or 3.")
        class_select = float(input("1 = Fighter, 2 = Rogue, 3 = Mage: "))
        class_select = math.floor(class_select)
    else:
        if class_select == 1:
            print(" ")
            print("Primary: strength. Save: strength, constitution.")
        elif class_select == 2:
            print(" ")
            print("Primary: dexterity. Save: dexterity, intelligence.")
        else:
            print(" ")
            print("Wizard. Primary: intelligence. Save: intelligence, wisdom.")
    continue_key_press()
    # A summary for the player so far.
    print("The figure leans back in their chair.\n'So,' it says. 'Let's see...'")
    summary_early = float(input("Like a summary? 1 = Yes, Other Number = No: "))
    summary_early = math.floor(summary_early)
    # Calls the summary function - can be used again later if the player wants.
    if summary_early == 1:
        print(get_early_summary(class_select, name_player, race_select))
    else:
        print("'Moving on then,' says the figure. 'We can ask again later...'")
    continue_key_press()
    # Explanation of dice rolling.
    print(" ")
    print("The figure produces a bag.")
    print("'Let's decide your fate.'\n'How strong are you really? How smart?'")
    continue_key_press()
    print("Out of the bag, the figure pulls four six-sided dice.")
    print("'You will roll these 6 times.'")
    continue_key_press()
    print("'We will add the cumulative total of the highest 3 dice six times.'")
    print("'Each of these six sums can be used as one of your 6 ability scores.'")
    question_roll = float(input("Roll the dice by pressing 1: "))
    question_roll = math.floor(question_roll)
    # Calls the dice roll function and passes the user's request to roll.
    dice_roll = roll_six_side_die_four_times(question_roll)
    print(dice_roll)
    # Asks the user to do their own math... probably a bad idea.
    roll_one = float(input("Enter the sum of the three highest values: "))
    roll_one = math.floor(roll_one)
    continue_key_press()
    print("The figure says, 'Easy, right?")
    # Same as above but does it five times.
    question_roll_two = float(input("Roll five more times by pressing 1: "))
    dice_roll = roll_six_side_die_four_times(question_roll_two)
    print(dice_roll)
    roll_two = float(input("Enter the sum of the three highest values: "))
    roll_two = math.floor(roll_two)
    dice_roll = roll_six_side_die_four_times(question_roll_two)
    print(dice_roll)
    roll_three = float(input("Enter the sum of the three highest values: "))
    roll_three = math.floor(roll_three)
    dice_roll = roll_six_side_die_four_times(question_roll_two)
    print(dice_roll)
    roll_four = float(input("Enter the sum of the three highest values: "))
    roll_four = math.floor(roll_four)
    dice_roll = roll_six_side_die_four_times(question_roll_two)
    print(dice_roll)
    roll_five = float(input("Enter the sum of the three highest values: "))
    roll_five = math.floor(roll_five)
    dice_roll = roll_six_side_die_four_times(question_roll_two)
    print(dice_roll)
    roll_six = float(input("Enter the sum of the three highest values: "))
    roll_six = math.floor(roll_six)
    continue_key_press()
    print("The figure scoops up the dice.\n'That was the last...'")
    continue_key_press()
    print("Your ability rolls are:")
    print(roll_one, roll_two, roll_three, roll_four, roll_five, roll_six)
    continue_key_press()
    print("The figure draws six cards.")
    print("And it says, 'You have six ability scores.'")
    print("Strength, dexterity, constitution, intelligence, wisdom, & charisma.")
    print("'You will place each of your rolls into each category.'")
    continue_key_press()
    print("It is important to review your current character attributes.")
    summary_early = float(input("Like a summary? 1 = Yes, Other Number = No: "))
    summary_early = math.floor(summary_early)
    # Calls the summary function for review.
    if summary_early == 1:
        print(get_early_summary(class_select, name_player, class_select))
        print("Oh, and of course, your ability rolls are:")
        print(roll_one, roll_two, roll_three, roll_four, roll_five, roll_six)
    else:
        print("'Moving on then,' says the figure.")
        print("Your ability rolls are:")
        print(roll_one, roll_two, roll_three, roll_four, roll_five, roll_six)
    continue_key_press()
    print("'Enter the desired roll sum into each of the following statistics.'")
    player_str = int(input("Enter your strength: "))
    player_str = math.floor(player_str)
    player_dex = int(input("Enter your dexterity: "))
    player_dex = math.floor(player_dex)
    player_con = int(input("Enter your constitution: "))
    player_con = math.floor(player_con)
    player_int = int(input("Enter your intelligence: "))
    player_int = math.floor(player_int)
    player_wis = int(input("Enter your wisdom: "))
    player_wis = math.floor(player_wis)
    player_cha = int(input("Enter your charisma: "))
    player_cha = math.floor(player_cha)
    continue_key_press()
    # Prints the user's unique stats based on race selection.
    # Uses shortcuts and relational operators.
    if race_select == 1:
        player_str += 2
        player_con += 1
        print(" ")
        print("'Such a strong Half-Orc, aren't we?'")
        # Contains end to put this all on one line.
        print("Str:", player_str, "Dex:", player_dex, "Con:", player_con, end=" ")
        print("Int:", player_int, "Wis:", player_wis, "Cha:", player_cha)
    elif race_select == 2:
        player_str += 1
        player_dex += 1
        player_con += 1
        player_int += 1
        player_wis += 1
        player_cha += 1
        print(" ")
        print("'What a jack-of-all trades, eh, Human?'")
        print("Str:", player_str, "Dex:", player_dex, "Con:", player_con, end=" ")
        print("Int:", player_int, "Wis:", player_wis, "Cha:", player_cha)
    elif race_select == 3:
        player_dex += 2
        print(" ")
        print("'I keep losing sight of you, little Halfling...'")
        print("Str:", player_str, "Dex:", player_dex, "Con:", player_con, end=" ")
        print("Int:", player_int, "Wis:", player_wis, "Cha:", player_cha)
    continue_key_press()
    print("The figure is pleased. It's cloak ruffles.")
    print("'Now, how much damage can you take?'")
    print("This is based on your class selection and your constitution.")
    continue_key_press()
    if class_select == 1:
        hit_die = 10
        # A lot of what's going on here is getting these trailing else in place.
        # Contains and as well as tests for greater than, less than, equal to, etc.
        # I know these can be simplified, but I needed *and* statements.
        if player_con < 10:
            hit_points = hit_die - 1
        elif player_con >= 10 and player_con <= 11:
            hit_points = hit_die
        elif player_con >= 12 and player_con <= 13:
            hit_points = hit_die + 1
        elif player_con >= 14 and player_con <= 15:
            hit_points = hit_die + 2
        elif player_con >= 16 and player_con <= 17:
            hit_points = hit_die + 3
        elif player_con >= 18 and player_con <= 19:
            hit_points = hit_die + 4
        else:
            hit_points = hit_die + 5
        print("'What a beefy fighter.'")
        print("Your hit points are: ", hit_points)
    elif class_select == 2:
        hit_die = 8
        if player_con < 10:
            hit_points = hit_die - 1
        elif player_con >= 10 and player_con <= 11:
            hit_points = hit_die
        elif player_con >= 12 and player_con <= 13:
            hit_points = hit_die + 1
        elif player_con >= 14 and player_con <= 15:
            hit_points = hit_die + 2
        elif player_con >= 16 and player_con <= 17:
            hit_points = hit_die + 3
        elif player_con >= 18 and player_con <= 19:
            hit_points = hit_die + 4
        else:
            hit_points = hit_die + 5
        print("'What a lithe rogue.'")
        print("Your hit points are: ", hit_points)
    else:
        hit_die = 6
        if player_con < 10:
            hit_points = hit_die - 1
        elif player_con >= 10 and player_con <= 11:
            hit_points = hit_die
        elif player_con >= 12 and player_con <= 13:
            hit_points = hit_die + 1
        elif player_con >= 14 and player_con <= 15:
            hit_points = hit_die + 2
        elif player_con >= 16 and player_con <= 17:
            hit_points = hit_die + 3
        elif player_con >= 18 and player_con <= 19:
            hit_points = hit_die + 4
        else:
            hit_points = hit_die + 5
        print("'What a frail wizard.'")
        print("Your hit points are: ", hit_points)
    continue_key_press()
    print("The figure pauses for a moment.")
    # Not statement.
    x = hit_points
    if not x > 10:
        print("It says, 'You'll probably be fine...'")
        continue_key_press()
    else:
        print("It says, 'I'm a bit worried about you...'")
        continue_key_press()
    # I'm going to use the remaining operators here to assign some equipment.
    print("The cloaked figure places the cards and dice back in the bag.")
    print("'You're about ready... but you need some equipment and... help.'")
    continue_key_press()
    print("The figure produces a crystal out of thin air.")
    print("'This is not all I can conjure... I need some information first.'")
    continue_key_press()
    print("The cloaked figure is going to ask you some questions.")
    print("Your answers will determine *random* boons you get for your quest.")
    continue_key_press()
    print("'Let us begin...'")
    continue_key_press()
    # I can just put floor around the input...
    player_pet = math.floor(float(input("Numeric value of your birth month?: ")))
    player_tunic = math.floor(float(input("What is your age?: ")))
    player_henchman = math.floor(float(input("How many siblings do you have?: ")))
    player_deity = math.floor(float(input("How tall are you? Nearest foot?: ")))
    player_star = math.floor(float(input("Numeric value of your birthdate?: ")))
    continue_key_press()
    # Exponential by 2.
    player_pet = player_pet ** 2
    if player_pet <= 10 and player_pet >= 60:
        player_pet = "Dog"
        print("You own a: ", player_pet)
    else:
        player_pet = "Cat"
        print("You own a: ", player_pet)
    # Multiplies by 10.
    player_tunic = player_tunic * 10
    if player_tunic > 240 and player_tunic < 400:
        player_tunic = "Cold Resistant Tunic"
        print("You are wearing a: ", player_tunic)
    else:
        player_tunic = "Heat Resistant Tunic"
        print("You are wearing a: ", player_tunic)
    # Divides by 10.
    player_henchman = player_henchman / 10
    if player_henchman > 0:
        player_henchman = "Demon"
        print("You are followed by a: ", player_henchman)
    else:
        player_henchman = "Spirit"
        print("You are followed by a: ", player_henchman)
    # Modulus or remainder of this equation will give me
    # a single digit number if people aren't...  20 feet tall
    player_deity = player_deity * 666 % 10
    if player_deity < 5:
        player_deity = "Tyr"
        print("You worship: ", player_deity)
    else:
        player_deity = "Bane"
        print("You worship: ", player_deity)
    # floor division with the largest possible integer returned
    player_star = player_star * 777 // 10
    if player_star > 500:
        player_star = "Northern Hemisphere"
        print("You were born under the: ", player_star)
    else:
        player_star = "Southern Hemisphere"
        print("You were born under the: ", player_star)
    # We're at the final step where the player's
    # information is all summarized for them.
    continue_key_press()
    print("The cloaked figure comes out of it's trance.")
    print("'Easy as that...'")
    print("It leans forward in the chair and grabs your hand.")
    continue_key_press()
    print("'I hope you are ready for your adventure...'")
    print("And with a shimmer in the air, the figure is gone.")
    print("You feel emboldened, like you know yourself better than ever before.")
    continue_key_press()
    # Dumps the whole sheet out here.
    print("YOUR CHARACTER SHEET")
    print(" ")
    print("YOUR NAME:", name_player)
    if race_select == 1:
        print("RACE: HALF-ORC")
    elif race_select == 2:
        print("RACE: HUMAN")
    else:
        print("RACE: HALFLING")
    if class_select == 1:
        print("CLASS: FIGHTER")
    elif class_select == 2:
        print("CLASS: ROGUE")
    else:
        print("CLASS: WIZARD")
    print("STR: ", player_str, "DEX: ", player_dex, "CON: ", player_con)
    print("INT: ", player_int, "WIS:", player_wis, "CHA: ", player_cha)
    print("HIT POINTS:", hit_points)
    print("PET:", player_pet)
    print("TUNIC:", player_tunic)
    print("HENCHMAN:", player_henchman)
    print("DEITY:", player_deity)
    print("BORN UNDER WHICH STARS:", player_star)
    continue_key_press()
    print("...")
    print("A familiar voice says, 'Good luck.'")
    print("And with that, thank you for generating your character with me.")
    print("This should be enough to get you started on D&D adventure.")
    # Had to add this because when I ran it with the interpreter it just closed...
    input("Press any key to close the program and get back to the real world: ")

# CALL TO MAIN #


main()