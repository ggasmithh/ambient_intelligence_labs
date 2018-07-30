import pymysql.cursors

# gets our connection to the database
def get_connection():
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='user',
                                 password='passwd',
                                 db='python-lab4',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    return connection


def show_tasks():

    #open the connection to the database
    connection = get_connection()

    sql = "SELECT * FROM task;"

    try:
        cursor = connection.cursor()
        cursor.execute(sql)

        tasks = []

        for row in cursor:
            tasks.append((row["id"], row["todo"]))

        if not tasks:
            tasks = ["No tasks found"]

    finally:
        connection.close()
        return tasks


# function to insert a new task
def insert_task(task_desc):

    #open the connection to the database
    connection = get_connection()

    sql = "INSERT INTO task (todo) VALUES (%s);"

    try:
        cursor = connection.cursor()
        cursor.execute(sql, task_desc)
        connection.commit()

    finally:
        connection.close()

# function to remove a specific task
def delete_task(tid):
    
    #open the connection to the database
    connection = get_connection()

    sql_delete = "DELETE FROM task WHERE id = %s;"

    try:
        cursor = connection.cursor()
        cursor.execute(sql_delete, tid)
        connection.commit()

    finally:
        connection.close()

