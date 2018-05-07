import pymysql.cursors

# gets our connection to the database
def get_connection():
    connection = pymysql.connect(user='user',
                                 password='passwd',
                                 unix_socket='/run/mysqld/mysqld.sock',
                                 db='python-lab4',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    return connection



def show_tasks(tid = -1):

    #open the connection to the database
    connection = get_connection()

    try:
        cursor = connection.cursor()

        #if no task id is specified, return all tasks
        if tid ==  -1:
            sql = "SELECT * FROM task;"
            cursor.execute(sql)
        
        #else, just get the task the user specified.
        else:
            sql = "SELECT * FROM task WHERE id = %s;"
            cursor.execute(sql, tid)

        tasks = cursor.fetchall()

    finally:
        connection.close()
        return tasks


# function to insert a new task
def insert_task(task_desc, urgent):

    #open the connection to the database
    connection = get_connection()

    sql = "INSERT INTO task (todo, urgent) VALUES (%s, %s);"

    try:
        cursor = connection.cursor()
        cursor.execute(sql, (task_desc, urgent))
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

    #return False on failure
    except:
        return False    
        
    #close connection and return True on successful delete
    finally:
        connection.close()
        return True
