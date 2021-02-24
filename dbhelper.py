import mysql.connector

class DBHelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost",user="root",password="",database="tinder")
            self.mycursor = self.conn.cursor()
        except:
            print("database error")
        else:
            print("connected to database")

    def insert(self,name,email,password):

        self.mycursor.execute("INSERT INTO users VALUES (NULL,'{}','{}','{}')".format(name,email,password))
        self.conn.commit()

    def search(self,email,password):
        self.mycursor.execute("SELECT * FROM users WHERE email = '{}' AND password = '{}'".format(email,password))
        data = self.mycursor.fetchall()
        return data
