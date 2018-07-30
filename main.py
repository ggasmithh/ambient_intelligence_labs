def math():

    print("Enter two numbers to get the sum!")

    num1 = int(input("Num. 1: "))
    num2 = int(input("Num. 2: "))

    print("The sum of your numbers is", num1 + num2)


def string_exp():

    print("Enter a string and we are gonna do some whacky stuff with it\n"
          "(We will return the first two and last two letters of the string)")

    string = input("string: ")

    if len(string) < 2:
        print("")

    else:
        print(string[:2] + string[ len(string) - 2 :])



def todo_manager():

    run = True
    tasks = []

    while run:

        user_choice = int(input("Type the number corresponding to the action you wish to perform:\n"
                            "1. Add new task;\n"
                            "2. Remove task;\n"
                            "3. Show all tasks;\n"
                            "4. Close program;\n"
                            "> "))


        if user_choice == 1:

            new_task = input("Type new task\n"
                             "> ")

            tasks.append(new_task)

        elif user_choice == 2:

            del_task = input("Type the task you wish to remove\n"
                             "> ")

            tasks.remove(del_task)


        elif user_choice == 3:

            for x in tasks:
                print(x, "\n")

        else:
            run = False


todo_manager()
