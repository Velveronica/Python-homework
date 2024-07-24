
from sqlalchemy import create_engine
from sqlalchemy.sql import text

class EmployeeTable:
    
    def __init__(self, connection_string):

        self.db=create_engine(connection_string)

    def get_emp(self):
        
        return self.db.execute("select * from employee where company_id=14732").fetchall()
    
    def delete(self, id):

        self.db.execute(f"delete from employee where id ={id}")

    def get_emp_id(self, id):

        return self.db.execute(f"select * from employee where company_id=14732 and id={id}").fetchall()
    
    def get_maxid(self):

        return self.db.execute(f"select max(id) from employee where company_id=14732").fetchall()[0][0]





        