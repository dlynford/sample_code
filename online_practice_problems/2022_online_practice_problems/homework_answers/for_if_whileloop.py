# 1/31/2022

def main():
    print('This is the main module.')


if __name__ == '__main__':
    main()

    #I put the input statement outside the while loop originally.
    #That kept the loop running forever! Whoops.
    # number = int(input("Enter an integer between 1 & 8: "))
    while True:
        number = input("Enter an integer between 1 & 8: ")
        if number == "quit":
            break
        number = int(number)
        if number < 1:
            print(f"{number} is less than 1. Try Again.")
        elif number <= 8:
            for integer in range(1, number + 1):
                print(integer)
        else:
            print(f"{number} is greater than 8. Try again.")
    print('Done')


