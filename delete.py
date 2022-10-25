import db_connection as dbConn;

class Delete:
    def func_DeleteData(self):
        connection = dbConn.getConnection()

        id = input('Enter Employee Id = ')
    
        try:
           sql = "Select * From Employee Where Id = ?" 
           cursor = connection.cursor()
           cursor.execute(sql, [id])
           item = cursor.fetchone()
           print('Data Fetched for Id = ', id)
           print('ID\t\t Name\t\t\t Age')
           print('-------------------------------------------')       
           print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
           print('-------------------------------------------')
           confirm = input('Are you sure to delete this record (Y/N)?')

           if confirm == 'Y':
               deleteQuery = "Delete From Employee Where Id = ?"
               cursor.execute(deleteQuery,[id])
               connection.commit()
               print('Data deleted successfully!')
           else:
                print('Wrong Entry')
        except:
            print('Somethng worng, please check')
        finally:
            connection.close()
