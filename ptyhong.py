import sqlite3
conn = sqlite3.connect('food.db')


cursor_obj = conn.cursor()
cursor_obj.execute("SELECT * FROM swiggytable")
output = cursor_obj.fetchall()
for row in output:
    print(row)