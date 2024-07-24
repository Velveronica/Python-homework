
import pytest
import requests
from employeeApi import EmployeeApi
from emp_table import EmployeeTable

db_connection_string ="postgres://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"

api=EmployeeApi("https://x-clients-be.onrender.com")
db=EmployeeTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

def test_get_emp():

    api_result=api.get_list_emp(params_to_add={'company': 14732})

    db_result=db.get_emp()

    assert len(api_result)==len(db_result)

def test_add_emp():


    body=api.get_list_emp(params_to_add={'company': 14732})
    len_before=len(body)


    id=668
    firstName="Veronica" 
    lastName="Procopets" 
    middleName="Vadimovna" 
    companyId=14732
    email="VV@mail.ru"
    phone="86666666666"
    birthdate= "2024-07-22T11:10:27.947Z"


    result=api.create_emp(firstName, lastName, middleName, email, phone, id, companyId=companyId, birthdate=birthdate)
    emp_id=result.json()["id"]
 #   assert result.status_code==201

    body=api.get_list_emp(params_to_add={'company': 14732})
    len_after=len(body)

 #   db.delete(id)
    body_db=db.get_emp_id(emp_id)
    
    assert len_after-len_before==1
    
    assert body_db[-1][0]==emp_id

def test_del():

    len_before=len(api.get_list_emp(params_to_add={'company': 14732}))

    maxid=db.get_maxid()
    db.delete(maxid)

    len_after=len(api.get_list_emp(params_to_add={'company': 14732}))

    assert len_before-len_after==1
