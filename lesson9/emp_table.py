
import allure
from sqlalchemy import create_engine
from sqlalchemy.sql import text

@allure.epic("БД сотрудники") 
@allure.severity("blocker")

class EmployeeTable:
    
    def __init__(self, connection_string):

        self.db=create_engine(connection_string)

    @allure.step("БД. Получить список сотрудников компании с id=14732 из БД")
    def get_emp(self):
        
        return self.db.execute("select * from employee where company_id=14732").fetchall()
    
    @allure.step("БД. Удаление сотрудника по {id} из БД")
    def delete(self, id: int):

        self.db.execute(f"delete from employee where id ={id}")

    @allure.step("БД. Получить сотрудника по {id} компании с id=14732 из БД")
    def get_emp_id(self, id: int):

        return self.db.execute(f"select * from employee where company_id=14732 and id={id}").fetchall()
    
    @allure.step("БД. Получить сотрудника с максимальным id из БД")
    def get_maxid(self):

        return self.db.execute(f"select max(id) from employee where company_id=14732").fetchall()[0][0]





        