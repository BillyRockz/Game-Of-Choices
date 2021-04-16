
'''This game gives you different options that would take you through a different path. '''

alpha = False

while not alpha:
 print("-- Welcome to the Game of Choices! --")
 print("-- Choose wisely! --"
          "-"
          "-")
 name = input("What is your name?: ")
 if name.isalpha():
  print("")
  print("-- That's a great name, " + name + "!")
  alpha = True
 else:
  print('your name has to be all letters. Try again')


 print("")
 print("You have been abducted by the aliens!")
 print("You wake up alone in a room and see two buttons")
 print("One is red, one is blue")
 first_question = True
 while first_question == True:
     answer_1 = input("Which one do you press?: ")
     if answer_1.lower().strip() == "red":
         print("*Zap* You are teleported and see aliens coming for you!")
         first_question = False
         second_question = True
         while second_question == True:
             answer_2 = input("Do you run or hide?: ")
             if answer_2.lower().strip() == "run":
                 print("")
                 print("*YOU'VE BEEN SHOT BY A LASER*")
                 print("--- GAME OVER ---")
                 print("")
                 alpha = False
                 second_question = False
             elif answer_2.lower().strip() == "hide":
                 print("You hide in a room with a big lever")
                 second_question = False
                 third_question = True
                 while third_question == True:
                     answer_3 = input("Do you pull it? (yes/no): ")
                     if answer_3.lower().strip() == "yes":
                         print("")
                         print("*YOU'VE BEEN RETURNED TO EARTH SAFELY*")
                         print("--- GAME OVER ---")
                         print("")
                         alpha = False
                         third_question = False
                     elif answer_3.lower().strip() == "no":
                         print("*THE ALIENS FOUND YOU AND YOU ARE DEAD*")
                         print("--- GAME OVER ---")
                         print("")
                         alpha = False
                         third_question = False
                     else:
                         print("That is not an option...")

             else:
                 print("That is not an option...")
     elif answer_1.lower().strip() == "blue":
         print("Oh no!! the room is on fire!")
         first_question = False
         second_question = True
         while second_question == True:
             answer_2 = input("Do you run or stay?: ")
             if answer_2.lower().strip() == "stay":
                 print("")
                 print("*YOU'VE BEEN INCINERATED*")
                 print("--- GAME OVER ---")
                 print("")
                 alpha = False
                 second_question = False
             elif answer_2.lower().strip() == "run":
                 print("You get to a room with two doors")
                 second_question = False
                 third_question = True
                 while third_question == True:
                     answer_3 = input("Do you go left or right?: ")
                     if answer_3.lower().strip() == "left":
                         print("")
                         print("*YOU'VE BEEN RETURNED TO EARTH SAFELY*")
                         print("--- GAME OVER ---")
                         print("")
                         alpha = False
                         third_question = False
                     elif answer_3.lower().strip() == "right":
                         print("*THE ALIENS FOUND YOU AND YOU ARE DEAD*")
                         print("--- GAME OVER ---")
                         print("")
                         alpha = False
                         third_question = False
                     else:
                         print("That is not an option...")
             else:
                 print("That is not an option...")
     else:
         print("That is not an option...")



