print("Welcome to the quiz!")
play = input("Do you want to play? ")
correct = 0
incorrect = 0
if(play.lower() == "yes"):
    print("Okay ! lets play ")
    first = input("\nWhich planet is known as Red Planet? \n A) Earth \n B) Mars \n C) Jupiter \n D) Venus \nEnter your option : ")
    if(first.upper() == "B"):
        print("correct")
        correct += 1
    else:
        print("incorrect")
        incorrect += 1
    second = input("How many days are there in a leap year? \n A) 365 \n B) 366 \n C) 364 \n D) 360 \nEnter your option : ")  
    if(second.upper() == "B"):
        print("correct")
        correct += 1
    else:
        print("incorrect")
        incorrect += 1
    third = input("Which is the largest ocean in the world? \n A) Indian Ocean \n B) Arctic Ocean \n C) Atlantic ocean \n D) Pacific Ocean \nEnter your option : ")  
    if(third.upper() == "D"):
        print("correct")
        correct += 1
    else:
        print("incorrect")
        incorrect += 1
    fourth = input("How many continents are there in the world? \n A) 5 \n B) 6 \n C) 7 \n D) 8 \nEnter your option : ")  
    if(fourth.upper() == "C"):
        print("correct")
        correct += 1
    else:
        print("incorrect")
        incorrect += 1
        
    percentage = (correct/4)*100
    print("\nCorrect answers :" + str(correct)+"\nIncorrect answers : "+str(incorrect)+"\nPercentage obtained : "+str(percentage)+"%")
else:
    print("Exiting the quiz.")
 