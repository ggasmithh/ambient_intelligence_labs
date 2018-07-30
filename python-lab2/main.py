from sys import argv

#sources used
#sys.argv: http://www.pythonforbeginners.com/system/python-sys-argv

#file I/0: https://stackoverflow.com/questions/6648493/open-file-for-both-reading-and-writing
#  https://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines

#get the first argument (that isnt the script name itself) passed from the commandline
user_file = argv[1]

#open the file for reading and writing
with open(user_file, "r+") as taskfile:

    run = True
    
    #put the contents of the file into a list, removing newline characters
    tasks = taskfile.read().splitlines()

    while run:

        user_choice = int(input("Type the number corresponding to the action you wish to perform:\n"
                            "1. Add new task;\n"
                            "2. Remove task;\n"
                            "3. Show all tasks;\n"
                            "4. Close program;\n"
                            "> "))


        if user_choice == 1:

            new_task = str(input("Type new task\n"
                             "> "))

            tasks.append(new_task)

        elif user_choice == 2:

            substring = input("Type a substring of the task you wish to remove\n"
                             "> ")

            for task in tasks:
                if substring in task:
                    tasks.remove(task)


        elif user_choice == 3:

            for task in tasks:
                print(task)


        else:

            # go to the beginning of the buffer so we overwrite instead of append
            taskfile.seek(0)
            taskfile.truncate()

            #write the tasks in our list to the actual file
            for task in tasks:
                taskfile.write(task + '\n')


            run = False

