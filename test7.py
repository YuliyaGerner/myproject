import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="9541",
  database="db1"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE food (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), calories smallint UNSIGNED)")

#sql = "INSERT INTO food (name, calories) VALUES (%s, %s)"
#val = ("pizza", "266")
#mycursor.execute(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record inserted.")

#mycursor.execute("SELECT * FROM food")

#myresult = mycursor.fetchall()

#for x in myresult:
  #print(x)

#mycursor.execute("ALTER TABLE users ADD COLUMN food VARCHAR(50) NOT NULL")

#mycursor.execute("DESCRIBE users")

#for x in mycursor:
  #print(x)


#sql = "SELECT \
 # users.name AS user, \
 # food.name AS food \
  #FROM users \
  #INNER JOIN food ON users.food = food.id"

#mycursor.execute(sql)

#myresult = mycursor.fetchall()

#for x in myresult:
  #print(x)

