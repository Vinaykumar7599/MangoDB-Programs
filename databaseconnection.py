import db_connection as dbConn

class Create:
    def func_CreateData(self):

        connection = dbConn.getConnection()
                
        name = input('Enter Name = ')
        age = input('Enter Age = ')

        try:
           query = "Insert Into Employee(Name, Age) Values(?,?)" 
           cursor = connection.cursor()

           cursor.execute(query, [name, age])

           connection.commit()
           print('Data Saved Successfully')

        except:
             print('Somethng worng, please check')

        finally:
           connection.close()
