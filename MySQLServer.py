import mysql.connector

try:

    #connect with database

    connection = mysql.connector.connect(

        host = "localhost",
        user = "root",
        password = "0715990719Pk!!?"
    )

    mycursor = connection.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
    mycursor.close()
    connection.close()

except mysql.connector.Error as e:
    print(f"Error:", e)
