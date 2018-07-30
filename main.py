# excellent resource on pymysql
# https://o7planning.org/en/11463/connecting-mysql-database-in-python-using-pymysql

import pymysql.cursors
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# connect to our bot with our API token
updater = Updater(token='547869170:AAGthxc9Ny967Qx6j4rZsOcSf4pLWWlg1qc')

# just to make it easier to type since we will be using it a lot
dispatcher = updater.dispatcher


# handle the /start command
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi! I can help you manage a ToDo list!")


# let the dispacher know about our new handler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# start polling for events
updater.start_polling()


# set up handling of other commands
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


# gets our connection to the database
def getConnection():
    connection = pymysql.connect(host='localhost',
                                 user='user',
                                 password='passwd',
                                 db='python-lab4',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


# function to show all tasks, or return a message if there are none
def showTasks(bot, update):
    connection = getConnection()

    sql = "SELECT todo FROM task;"

    try:
        cursor = connection.cursor()
        cursor.execute(sql)

        tasks = []

        for row in cursor:
            tasks.append(row["todo"])

        if not tasks:
            bot.send_message(chat_id=update.message.chat_id, text="No tasks found")

        else:
            bot.send_message(chat_id=update.message.chat_id, text=('\n'.join(tasks)))

    finally:
        connection.close()


showTasks_handler = CommandHandler('showTasks', showTasks)
dispatcher.add_handler(showTasks_handler)


# function to insert a new task
def newTask(bot, update, args):
    # convert args from list to string
    args = " ".join(args)

    connection = getConnection()

    sql = "INSERT INTO task (todo) VALUES (%s);"

    try:

        cursor = connection.cursor()
        cursor.execute(sql, (args))

        connection.commit()

        bot.send_message(chat_id=update.message.chat_id, text="New Task Added.")

    finally:
        connection.close()


newTask_handler = CommandHandler('newTask', newTask, pass_args=True)
dispatcher.add_handler(newTask_handler)


# function to remove all tasks matching substring
def removeAllTasks(bot, update, args):
    # convert args from list to string
    args = " ".join(args)

    # list of tasks with substring
    found_tasks = []

    connection = getConnection()

    sql = "SELECT todo FROM task;"
    sql_delete = "DELETE FROM task WHERE todo = %s;"

    try:
        cursor = connection.cursor()
        cursor.execute(sql)

        for row in cursor:
            if args in row["todo"]:
                found_tasks.append(row["todo"])

        if len(found_tasks) != 0:
            for task in found_tasks:
                cursor.execute(sql_delete, (task))

            # make a string containing our deleted tasks
            deleted_tasks = "Tasks \"" + "\", \"".join(found_tasks) + "\" deleted."

            bot.send_message(chat_id=update.message.chat_id, text=deleted_tasks)

            connection.commit()

        else:
            bot.send_message(chat_id=update.message.chat_id, text="Task(s) not found.")

    finally:
        connection.close()


removeAllTasks_handler = CommandHandler('removeAllTasks', removeAllTasks, pass_args=True)
dispatcher.add_handler(removeAllTasks_handler)


# function to remove a specific task
def removeTask(bot, update, args):
    # convert args from list to string
    args = " ".join(args)
    connection = getConnection()

    # we need this so we can tell the user if the task they want to delete even exists
    sql_find = "SELECT todo FROM task"

    # this will actually delete the task
    sql_delete = "DELETE FROM task WHERE todo = %s;"

    try:
        cursor = connection.cursor()
        cursor.execute(sql_find)

        # create list of found tasks
        found = []
        for row in cursor:
            found.append(row["todo"])

        # if the value is found, delete it...
        if args in found:
            cursor.execute(sql_delete, (args))
            bot.send_message(chat_id=update.message.chat_id, text="Task successfully removed")
            connection.commit()

        # ...if not, tell the user that it wasn't found
        else:
            bot.send_message(chat_id=update.message.chat_id, text="Specified task not found")

    finally:
        connection.close()


removeTask_handler = CommandHandler('removeTask', removeTask, pass_args=True)
dispatcher.add_handler(removeTask_handler)