# 2/16/2022
# 3.Write a program to display only those numbers from a list that satisfy the following conditions
# •	The number must be divisible by five
# •	If the number is greater than 150, then skip it and move to the next number
# •	If the number is greater than 500, then stop the loop

while True:
    a = int(input("Enter an integer between 1 and 500: "))
    while a < 1 or a > 500:
        a = int(input("Please enter an integer between 1 and 500: "))
    numbers = [i for i in range(1, a+1)]
    for number in numbers:
        if number % 5 == 0 and number <= 150:
            print(number)
        elif number % 5 != 0:
            continue
        if number > 150:
            print("skipping this number.")

        elif number > 500:
            print("The limit is 500.")

    a = input("Do you want to continue (y/n)? ").lower()
    if a == "n" or a == "no":
        print("Goodbye.")
        break

    if a == "y" or a == "yes":
        print("Great. Starting again.\n")
        # continue
    # else:
    #     print("invalid input")



