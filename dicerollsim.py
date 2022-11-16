#importing random
import random
print("Welcome to dice roll app.")
dice_range = 6
number_of_dices = 1
while True:
    general_process = str(input("-Enter \"roll\" to roll the dices.\nEnter \"settings\" to edit the settings.\nType Here:"))
# settings
    def settingsfunction():
        global dice_range
        global number_of_dices
        settings_process = str(input("\nWhat Would You Like To Change?"))
        if settings_process.lower() == "dice mode" or settings_process.lower() == "dm":
            try:
                dice_range = int(
                    input("What would you like your dice range to be?(Min.6-Max.39)-(Only use NUMBERS.):"))
            except ValueError:
                print("ONLY USE NUMBERS!")
            except:
                print("You've made mistake that has no bounds with value.Restart the app.")
        if settings_process.lower() == "number of dices" or settings_process.lower() == "nd":
            try:
                number_of_dices = int(input("How many dices yo need?(Min.1-Max.4)-(Only use NUMBERS."))
            except ValueError:
                print("ONLY USE NUMBERS!")
            except:
                print("You've made mistake that has no bounds with value.Restart the app.")
    if general_process.lower() == "settings":
        dice_mode = f"{dice_range}-roll dice"
        print(f'''
    Your Current Settings:
    -Dice Mode: {dice_mode}
    -Number of Dices: {number_of_dices}''')
        settingsfunction()
    diceroll_range = dice_range

    def dicerollingfunction(number_of_dices,diceroll_range):
        if number_of_dices == 1:
            dice1 = random.randint(1, diceroll_range)
            print("Result:", dice1)
        elif number_of_dices == 2:
            dice1 = random.randint(1, diceroll_range)
            dice2 = random.randint(1, diceroll_range)
            print("First Dice:", dice1)
            print("Second Dice:", dice2)
        elif number_of_dices == 3:
            dice1 = random.randint(1, dice_range)
            dice2 = random.randint(1, dice_range)
            dice3 = random.randint(1, dice_range)
            print("First Dice:", dice1)
            print("Second Dice:", dice2)
            print("Third Dice:", dice3)
        elif number_of_dices == 4:
            dice1 = random.randint(1, dice_range)
            dice2 = random.randint(1, dice_range)
            dice3 = random.randint(1, dice_range)
            dice4 = random.randint(1, dice_range)
            print("First Dice:", dice1)
            print("Second Dice:", dice2)
            print("Third Dice:", dice3)
            print(("Fouth Dice:", dice4))
    if general_process.lower() == "roll":
        print(dice_range,number_of_dices)
        print("DICES ARE ROLLING........")
        dicerollingfunction(number_of_dices,dice_range)
        play_again = str(input("Would you like to roll again,or change the settings?(Press ENTER to quit."))
        if play_again.lower() == "roll again" or play_again.lower() == "roll" or play_again.lower() == "r":
            dicerollingfunction()
        elif play_again.lower() == "change the settings" or play_again.lower() == "change  settings" or play_again.lower() == "settings" or play_again.lower() == "cs" or play_again.lower() == "s":
            settingsfunction()
        else:
            print("See you later!")









