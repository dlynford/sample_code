

welcome = input("You will be adding two numbers together. Do you want to start (y) or (n)? ").lower()
if welcome == "y" or welcome == "yes":

    while welcome == "y" or welcome == "yes":
        print("Add two numbers together.")
        ask = int(input("Number one: "))
        ask_again = int(input("Number two: "))
        total = ask + ask_again
        print(total)
        welcome = input("\nDo you want to continue (y) or (n)? ").lower()
        if welcome == "n" or welcome == "no":
            print("Goodbye.")
            break
        elif welcome == "y" or welcome == "yes":
            continue
            # print("ok")
        else:
            print('invalid input.')

elif welcome == 'n' or welcome == "no":
    print("Okay maybe next time.")
else:
    print("invalid!")




