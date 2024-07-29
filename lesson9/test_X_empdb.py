
import allure
import pytest
import requests
from employeeApi import EmployeeApi
from emp_table import EmployeeTable


db_connection_string ="postgres://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"

api=EmployeeApi("https://x-clients-be.onrender.com")
db=EmployeeTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

@allure.id("SKYPRO-2")
@allure.story("Получение списка сотрудников")
@allure.feature("READ")
@allure.title("Получение списка сотрудников конкретной компании")
@allure.description("Запрос организация с параметром company = 14732")
def test_get_emp():

    with allure.step("Получить список сотрудников через API"):
         api_result=api.get_list_emp(params_to_add={'company': 14732})

    with allure.step("Получить список сотрудников через БД"):
         db_result=db.get_emp()

    with allure.step("Сравнить два списка"):
         assert len(api_result)==len(db_result)

@allure.id("SKYPRO-2")
@allure.story("Добавление сотрудника")
@allure.feature("CREATE")
@allure.title("Добавление сотрудника в компанию")
@allure.description("Запрос организация с параметром company': 14732")
def test_add_emp():

    with allure.step("Получить список сотрудников через API"):
        body=api.get_list_emp(params_to_add={'company': 14732})
        len_before=len(body)

    with allure.step("Создать нового сотрудника"):
        id=668
        firstName="Veronica" 
        lastName="Procopets" 
        middleName="Vadimovna" 
        companyId=14732
        email="VV@mail.ru"
        phone="86666666666"
        birthdate= "2024-07-22T11:10:27.947Z"
        result=api.create_emp(firstName, lastName, middleName, email, phone, id, companyId=companyId, birthdate=birthdate)
        
    with allure.step("Узнать {emp_id} нового сотрудника"):
        emp_id=result.json()["id"]

    with allure.step("Получить новый список сотрудников через API"):
        body=api.get_list_emp(params_to_add={'company': 14732})
        len_after=len(body)

        with allure.step("Получить список сотрудников через БД"):
            body_db=db.get_emp_id(emp_id)
    
    with allure.step("Проверить, что список увеличился на 1"):
        assert len_after-len_before==1
    
    with allure.step("Проверить, что новый сотрудник появился в БД"):
        assert body_db[-1][0]==emp_id

@allure.id("SKYPRO-2")
@allure.story("Удаление сотрудника")
@allure.feature("DELETE")
@allure.title("Удаление сотрудника конкретной компании")
@allure.description("Удаление последнего созданного сотрудника с параметром max_id, компании с параметром company = 14732")
def test_del():

    with allure.step("Получить список сотрудников через API"):
        len_before=len(api.get_list_emp(params_to_add={'company': 14732}))

    with allure.step("Получить сотрудника с {maxid} через БД"):
        maxid=db.get_maxid()

    with allure.step("Удалить сотрудника с {maxid} через БД"):
        db.delete(maxid)

    with allure.step("Получить новый список сотрудников через API"):
        len_after=len(api.get_list_emp(params_to_add={'company': 14732}))

    with allure.step("Сравнить два списка"):
        assert len_before-len_after==1
