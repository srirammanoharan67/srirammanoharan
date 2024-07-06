print("***************Guess the number********************")
player_regno = []
while True:
    click=input("Enter 'c' to play:")
    
    if click == "c":
        enter_id = int(input("Enter reg id: "))
        
        if enter_id in player_regno:
            print("You have already tried")#If reg_no exists you cant play again
            break
        else:
            player_regno.append(enter_id)  # Add new registration number
            guess = int(input("Guess between 1 and 50: "))
            
            if guess == 5:
                print("Your prize money: 500 $")
                print("Thanks for participating")
                break
            elif guess > 50:
                print("Guess below 50")
            
            click = input("Sorry, you didn't find the correct number. Try again (click 'c'): ")
            print("\n")
    else:
        print("Wrong input")
        break


