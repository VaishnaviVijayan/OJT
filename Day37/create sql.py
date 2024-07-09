#create a database
import sqlite3
conn = sqlite3.connect('article.db')
c=conn.cursor()
conn.close

#create a table in article.db database
import sqlite3
conn = sqlite3.connect('article.db')
c=conn.cursor()
c.execute("create table example(Software VARCHAR, Version Real,Price Real )")

#inserting the data into an example table
c.execute("Insert into example Values('Python',3.4,'100')")
c.execute("Insert into example Values('Adobe',10.2,'1000')")
c.execute("Insert into example Values('Office',16,'1000')")

#read the data from databse
sql = "select * from example"
for row in c.execute(sql):
    print("Software: "+row[0])
    print("Version: "+str(row[1]))
    print("Price: "+str(row[2]))
    
#Insert data dynamically in a database using the make method
def dynamic_data():
    software = input("Write Software Name : ")
    version = input("Write Versio : ")
    Price= input("Write Price")

c.execute("insert into example(Software,Version,Price) values(?,?,?)" ,(software,version,Price))
conn.commit()
dynamic_data()

#take another database handling with update the data in the database
sql="update example set Version = 3.5 where Software = 'Python'"
c.execute(sql)
sql = "select * from example"

for row in c.execute(sql):
    print(row)
    
#Another Example of perform detele operation
sql="delete from example where Software = 'Python'"
c.execute(sql)
sql = "select * from example"
for row in c.execute(sql):
    print(row)