import mysql.connector

from tabulate import tabulate

con = mysql.connector.connect(host="localhost", user="root", password="1234", database="covid19")
def insert():
    country = input("Enter country : ")
    total_cases = input("Enter total cases : ")
    new_cases = input("Enter new cases : ")
    total_death = input("Enter total_death : ")
    new_death = input("Enter new death : ")
    total_tests=input("Enter total tests  : ")
    population= input("Enter population : ")


    res = con.cursor()
    sql = "insert into covid_data (country,total_cases,new_cases,total_death,new_death,total_tests,population) values (%s,%s,%s,%s,%s,%s,%s)"
    res.execute(sql,(country, total_cases, new_cases,total_death,new_death,total_tests,population))
    con.commit()
    print("\n")
    print("Record Insert Successfully")


def select():
    res = con.cursor()
    sql = "SELECT * from covid_data"
    res.execute(sql)
    result = res.fetchall()
    print("\n")
    print(tabulate(result, headers=["ID", "COUNTRY", "TOTAL_CASES", "NEW_CASES","TOTAL_DEATH","NEW_DEATH", "TOTAL_TESTS", "POPULATION"]))



def update():
    print("1.Enter country")
    print("2.Enter total cases")
    print("3.Enter new case")
    print("4.Enter total_death")
    print("5.Enter new death")
    print("6.Enter total_tests")
    print("7.Enter population")
  
    option = int(input("\nWhich field you want to update?:"))
    if option == 1:
        id = input("Enter Your ID:")
        country = input("Enter Your country:")
        cur = con.cursor()
        sql = "UPDATE covid_data set country=%s where id=%s"
        cur.execute(sql, (country, id))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")

    elif option == 2:
        id = input("Enter Your ID:")
        total_cases = input("Enter Your total_cases:")
        cur = con.cursor()
        sql = "UPDATE covid_data set total_cases=%s where id=%s"
        cur.execute(sql, (total_cases, id))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
        
    elif option == 3:
        id = input("Enter Your ID:")
        new_cases = input("Enter Your new_cases:")
        cur = con.cursor()
        sql = "UPDATE covid_data set new_cases=%s where id=%s"
        cur.execute(sql, (new_cases, id))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
       
    elif option == 4:
        id = input("Enter Your ID:")
        total_death = input("Enter Your total_death:")
        cur = con.cursor()
        sql = "UPDATE covid_data set total_death=%s where id=%s"
        cur.execute(sql, (total_death, id))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
        
    elif option == 5:
        pid = input("Enter Your ID:")
        new_death = input("Enter Your new_death:")
        cur = con.cursor()
        sql = "UPDATE covid_data set new_death=%s where id=%s"
        cur.execute(sql, (new_death, id))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
    elif option == 6:
        id = input("Enter Your ID:")
        total_tests = input("Enter Your total_tests:")
        cur = con.cursor()
        sql = "UPDATE covid_data set total_tests=%s where id=%s"
        cur.execute(sql, (total_tests, id))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
    elif option == 7:
        id = input("Enter Your ID:")
        population = input("Enter Your population:")
        cur = con.cursor()
        sql = "UPDATE covid_data set population=%s where id=%s"
        cur.execute(sql, (population, id))
        con.commit()
        select()
        print("\n")
        print("Update Successfully")
    else:
        print("Invalid")

def delete():
    id = input("Enter Your ID:")
    res = con.cursor()
    sql = "delete from covid_data where id=%s"
    res.execute(sql,(id,))
    con.commit()
    print("\n")
    print("Record Deleted Successfully...!!!")



while True:
    print("\n")
    print("1.Insert Record")
    print("2.Select Record")
    print("3.Update Record")
    print("4.Delete Record")
    print("5.Exit")
    print("\n")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        insert()
    elif choice ==2:
        select()
    elif choice ==3:
        update()
    elif choice == 4:
        delete()
   
    elif choice == 5:
        quit()
    else:
        print("Invalid Option...!!!")

