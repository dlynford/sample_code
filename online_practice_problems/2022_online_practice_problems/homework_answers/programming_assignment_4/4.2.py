# 2/12/2022

# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number.
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

while True:
    total = 0
    result = ""
    ask = int(input("Enter a positive integer between 1 and 20: "))
    while ask < 1 or ask > 20:
        try:
            ask = int(input("Please enter a number between 1 and 20: "))
        except ValueError:
            print("\nStrings not accepted. Enter an integer between 1 and 20. ")

    for number in range(1, ask+1):
        total += number
    print(f"Sum = {total}")
    for i in range(1, ask+1):
        i = str(i)
        result += f"{i}+"
        # print(f"{i}+")
    print(result)

    ask = input("Do you want to continue? (y/n): ").lower()
    if ask == "n" or ask == "no":
        print("Goodbye.")
        break
    elif ask == "y" or ask == "yes":
        print("Continuing....\n")

    else:
        print("Invalid input.")

