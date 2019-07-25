'''
Created on Jul 2, 2019

@author: HI TECH
'''
import argparse
import pymysql

from prettytable import PrettyTable


class BaseClass():
    '''
    classdocs
    '''

    def __init__(self, id=None, name=None, category=None, salary=None):
        '''

        @summary: Constructor to identify the param
        @param id: integer unique value 
        @param name : name of employee
        @param Category:  the Category of employee (engineer or manger)
        @param salary: integer number , how much the Employee Catching salary

        '''
        self.id = id
        self.name = name
        self.category = category
        self.salary = salary

    def argumentParser(self):

        # Instantiate the parser
        parser = argparse.ArgumentParser(description="The server IP")

        parser.add_argument(
            '-s', "--server", help="The server name", type=int, default=0)
        parser.add_argument(
            '-i', "--id", help="The id", type=int, default=0)
        parser.add_argument(
            '-n', "--name", help="The name of employee", type=str, default="")
        parser.add_argument(
            '-sal', "--salary", help="The salary", type=int, default=0)

        # Parse the arguments
        arguments = parser.parse_args()
        return arguments

    # Connecting to the mysql
    def connectData(self):
        '''
        @summary: connecting data with mysql
        you need to add the user-name of the database and the password

        '''
        mydb = pymysql.connect(
            host="localhost",
            user="sawsan",
            passwd="Sawsan_123",
            db="employee"

        )
        mycursor = mydb.cursor()

        return mydb

    # insert the Employee info to the file
    def addEmployee(self, id, name, category, salary):
        '''
        @summary: take the parametres and add it to database
        @param id: integer unique value 
        @param name : name of employee
        @param Category:  the category of employee (engineer or manger)
        @param salary: integer number , how much the Employee Catching salary

        '''
        try:
            conn = self.connectData()
            mycursor = conn.cursor()
            id_list = mycursor.execute("SELECT id FROM employee")

        # check if the id in file
            # if the id in file
            if id in id_list:
                print("this {0} already added ", category)

            # if the id dosn't file
        except:
            sql = "INSERT INTO employee (id,name, category,salary ) VALUES (%s, %s,%s , %s)"
            val = (id, name, category, salary)
            mycursor.execute(sql, val)
            conn.commit()
            print("done")

    # get all employee in the file

    def getAllEmployees(self, category=None):
        '''
        @summary: display the Employees which in database 
        @param category:  the category of employee (engineer or manger)
        '''

        try:
            conn = self.connectData()
            mycursor = conn.cursor()

            if category is None:                          # print all employee
                mycursor.execute("SELECT * FROM employee")
                myresult = mycursor.fetchall()
                table = PrettyTable(['ID', 'Name', 'Catagory', 'Salary'])
                for list in myresult:
                    table.add_row([list[0], list[1], list[2], list[3]])

                print(table)

            else:
                # print specific employee
                sql = "SELECT * FROM employee where category=%s"
                val = (category,)
                myresult = mycursor.execute(sql, val)
                myresult = mycursor.fetchall()

                if not myresult:
                    print("Can't find any {category}".format(**locals()))
                else:
                    print(myresult)

        except Exception as e:
            print('Error: %s' % str(e))

    # get the salary from  specific id
    def getSalary(self, id):
        '''
        @summary: display the salary for specific id
        @param id: integer unique value 

        '''
        try:

            conn = self.connectData()
            mycursor = conn.cursor()
            sql = "SELECT id ,salary FROM employee where id=%s"
            val = (id,)
            myresult = mycursor.execute(sql, val)
            myresult = mycursor.fetchall()

            for item in myresult:
                if id in item:
                    salary_is = item[1]
                    print(
                        "the salary of this id is = {salary_is} ".format(**locals()))

            if not myresult:
                print("Can't find any id = {id}".format(**locals()))

        except Exception as e:
            print('Error: %s' % str(e))

    # remove the manger with specific id
    def removeEmployee(self, id):
        '''
        @summary: remove specific id from the database
        @param id: integer unique value
        '''

        try:
            conn = self.connectData()
            mycursor = conn.cursor()
            sql = "DELETE FROM employee WHERE id =%s"
            val = (id,)
            myresult = mycursor.execute(sql, val)
            if myresult:
                print("done")
                conn.commit()
            else:
                print("Can't find any id = {id}".format(**locals()))

        except Exception as e:
            print('Error: %s' % str(e))
