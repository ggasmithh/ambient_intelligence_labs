#https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-–-Your-first-Bot
#this article helped massively in the development of this bot


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#connect to our bot with our API token
updater = Updater(token='547869170:AAGthxc9Ny967Qx6j4rZsOcSf4pLWWlg1qc')

#just to make it easier to type since we will be using it a lot
dispatcher = updater.dispatcher

#handle the /start command
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi! I can help you manage a ToDo list!")

#let the dispacher know about our new handler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#start polling for events
updater.start_polling()

#set up handling of other commands
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

#function to show all tasks, or return a message if there are none
def showTasks(bot, update):
    with open("task_list.txt", "r+") as taskfile:

        # put the contents of the file into a list, removing newline characters
        tasks = taskfile.read().splitlines()

        if tasks:
            bot.send_message(chat_id=update.message.chat_id, text=tasks)

        else:
            bot.send_message(chat_id=update.message.chat_id, text="No Tasks")

showTasks_handler = CommandHandler('showTasks', showTasks)
dispatcher.add_handler(showTasks_handler)


#function to insert a new task
def newTask(bot, update, args):

    #convert args from list to string
    args = " ".join(args)

    with open("task_list.txt", "r+") as taskfile:

        # put the contents of the file into a list, removing newline characters
        tasks = taskfile.read().splitlines()
        tasks.append(args)

        # go to the beginning of the buffer so we overwrite instead of append
        taskfile.seek(0)
        taskfile.truncate()

        # write the tasks in our list to the actual file
        for task in tasks:
            taskfile.write(task + '\n')

    bot.send_message(chat_id=update.message.chat_id, text="New Task Added.")

newTask_handler = CommandHandler('newTask', newTask, pass_args=True)
dispatcher.add_handler(newTask_handler)


#function to remove all tasks matching substring
def removeAllTasks(bot, update, args):

    #convert args from list to string
    args = " ".join(args)

    with open("task_list.txt", "r+") as taskfile:

        # put the contents of the file into a list, removing newline characters
        tasks = taskfile.read().splitlines()

        found_tasks = []

        for task in tasks:
            if args in task:
                found_tasks.append(task)
                tasks.remove(task)

        if len(found_tasks) != 0:
            # go to the beginning of the buffer so we overwrite instead of append
            taskfile.seek(0)
            taskfile.truncate()

            # write the tasks in our list to the actual file
            for task in tasks:
                taskfile.write(task + '\n')

            #make a string containing our deleted tasks
            deleted_tasks = "Tasks \"" + "\", \"".join(found_tasks) + "\" deleted."

            bot.send_message(chat_id=update.message.chat_id, text=deleted_tasks)

        else:
            bot.send_message(chat_id=update.message.chat_id, text="Task(s) not found.")

removeAllTasks_handler = CommandHandler('removeAllTasks', removeAllTasks, pass_args=True)
dispatcher.add_handler(removeAllTasks_handler)


#function to remove a specific task
def removeTask(bot, update, args):

    #convert args from list to string
    args = " ".join(args)
    
    with open("task_list.txt", "r+") as taskfile:

        # put the contents of the file into a list, removing newline characters
        tasks = taskfile.read().splitlines()


        try:
            tasks.remove(args)

            # go to the beginning of the buffer so we overwrite instead of append
            taskfile.seek(0)
            taskfile.truncate()

            # write the tasks in our list to the actual file
            for task in tasks:
                taskfile.write(task + '\n')

            bot.send_message(chat_id=update.message.chat_id, text="Task successfully removed")

        except:
            bot.send_message(chat_id=update.message.chat_id, text="Specified task not found")

removeTask_handler = CommandHandler('removeTask', removeTask, pass_args=True)
dispatcher.add_handler(removeTask_handler)


#this will handle unknown commands
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Invalid Command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)