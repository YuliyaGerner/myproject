import mysql.connector as conn
db=conn.connect(user="root",passwd="9541")
cursor=db.cursor()
cursor.execute("create database if not exists user")
cursor.execute("use user")
cursor.execute("""CREATE TABLE if not exists login (
userid VARCHAR( 50 ) NOT NULL ,
password VARCHAR( 50 ) NOT NULL
)""")
while True:
    print("""Select your operation
1)signup
2)signin
3)exit""")
    ch=input("Enter your choice:")
    if ch=="1":
        user=input("Enter a userid:")
        password=input("Enter a password:")
        cursor.execute("insert into login values((%s),(%s))",(user,password))
        db.commit()
        print("\nYou have successfully registered\n")
    elif ch=="2":
        while True:
            uid=input("Enter a userid:")
            passwd=input("Enter a password:")
            user=[]
            password=[]
            cursor.execute("select userid from login")
            for i in cursor.fetchall():
                user.append(i[0])
            cursor.execute("select password from login")
            for i in cursor.fetchall():
                password.append(i[0])
            if uid in user:
                index=user.index(uid)
                if passwd==password[index]:
                    print("\nlogin successfull\n")
                    break
                else:
                    print("\nwrong password\n")
            else:
                print("\nuser doesn't exists\n")
    elif ch=="3":
        db.close()
        break