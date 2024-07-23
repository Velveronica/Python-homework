
from sqlalchemy import create_engine
from sqlalchemy.sql import text

class EmployeeTable:
    
    def __init__(self, connection_string):

        self.db=create_engine(connection_string)

    def get_emp(self):
        
        return self.db.execute("select * from employee").fetchall()
        