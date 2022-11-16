import sqlite3

command = "start"
#table name = emp
connection = sqlite3.connect('emp.db')
cursor = connection.cursor()
print("Welcome to sqlite3 command line.\n")

while(1):
    print("command: ")
    command = input()
    if(command == "exit"):
        break
    try:
        cursor.execute(command)
        connection.commit()
        ans = cursor.fetchall()
    
        for i in ans:
            print(i)
    except:
        print("SQL Command Error !")
connection.close()