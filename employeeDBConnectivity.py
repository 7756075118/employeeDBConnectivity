import mysql.connector

class Employee:

    def __init__(self):

        self.conn = mysql.connector.connect(

            host = "localhost",

            user = "root",

            password = "sakshi",

            database = "employeedb",

            port = "3306"

        )

        self.cur = self.conn.cursor()

        print("Connectivity done sucessfully!!")

    def fetch_data(self):

        query = "Select * from employeeTable"

        self.cur.execute(query)

        for row in self.cur.fetchall():

            print(row)

        print("Data has fetched Successfully!!")

    def inert_data(self):

        sql = "Insert into employeeTable values (%s,%s,%s)"

        values = [

            (1,"Krisha","HR"),

            (2,"Nidhi","Sales"),

            (3,"Prachi","CA")

        ]
        self.cur.executemany(sql,values)

        self.conn.commit()

        print("Data inserted Successfully!!")

    def delete_data(self):

        sql = "Delete from employeeTable where emp_id = %s"

        value = (1,)

        self.cur.execute(sql,value)

        self.conn.commit()

        print("Data deleted successfully!!")

    def close_connection(self):

        self.conn.close()

        print("Connection is closed!!")

e1 = Employee()

print("Options\n1.Fetch data.\n2.Insert data.\n3.Delete data.\n4.Exit.")

option = int(input("Enter option 1/2/3/4 : "))

if(option==1):

    e1.fetch_data()

elif(option==2):

    e1.inert_data()

elif(option==3):

    e1.delete_data()

elif(option==4):

    print("Exit")

else:

    print("Invalid option!!!")
    
    