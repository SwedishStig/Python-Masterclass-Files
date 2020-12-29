import sqlite3

db = sqlite3.connect("contacts.sqlite")
#db.execute("CREATE TABLE contacts(name TEXT, phone INTEGER, email TEXT)" )
db.execute("INSERT INTO contacts(name, phone, email) VALUES ('Eggman', 6545,'twitter dot com')")
db.execute("INSERT INTO contacts VALUES ('Junkrat', 1001,'boom@boom.boom')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
for row in cursor:
    print(row)
cursor.close()

find_name = input("Name to find: ")
for row in db.execute("SELECT * FROM contacts WHERE name LIKE ?", (find_name,)):
    print(row)

db.commit()
db.close()
