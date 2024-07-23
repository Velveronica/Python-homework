
import pytest
import requests
from employeeApi import EmployeeApi
from emp_table import EmployeeTable

db_connection_string ="postgres://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"

api=EmployeeApi("https://x-clients-be.onrender.com")
db=EmployeeTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

def test_get_emp():

    api_result=api.get_list_emp()

    db_result=db.get_emp()

    assert len(api_result)==len(db_result)

