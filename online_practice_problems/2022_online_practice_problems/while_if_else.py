2/2/2022

while True:
    number = int(input("Enter an integer between 1 & 8: "))

    while(number<1 or number>8):
        number = int(input("Please Enter an integer between 1 & 8: "))

    if (number >=1 and number <=8):
        print("Hey this is the number: ",number)
        for i in range(number):
            print(i)

    x = input("do you want to cont? ").lower()
    if(x == "n" or x == "no"):
        break
print("Done!")

