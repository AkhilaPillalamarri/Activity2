# Name: Akhila Pillalamarri(97960370)
# Course Name : 4900_Activity 3
# Date:01-30-2020
# Purpose : To calculate the grades from the  marks achieved by students

mark = 0;
Percentage = 0;

choice = "y"
while choice.lower() == "y":

    mark = float(input("Enter the points earned from 0-1000: "))   # Enter the marks
    Percentage = float((mark*100)/1000)                            # Calculating precentage obtained by the marks given


    if(mark<=1000 and mark>=0):                                    # If the marks entered are less than 1000 and greater than 0 enters into loop
        print("Percentage is " + str(Percentage))
        if (Percentage>=92):
             print("Letter Grade : A")
        elif (Percentage>=88) and (Percentage<=91.99):
            print("Letter grade : B+")
        elif (Percentage>=82) and (Percentage<=87.99):
            print("Letter grade : B")
        elif (Percentage>=78) and (Percentage<=81.99):
             print("Letter grade : C+")
        elif (Percentage>=70) and (Percentage<=77.99):
             print("Letter grade : C")
        elif (Percentage>=60) and (Percentage<=69.99):
             print("Letter grade : D")
        else:
            print("Letter grade : F")
    else:                                                     # If invalid score enters prints invalid score and asks for choice to continue
        print("Invalid score entered")

    choice = input("Would you like to try again?: ").lower()

print("bye")