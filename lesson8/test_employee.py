
import pytest
import requests
from employeeApi import EmployeeApi

api=EmployeeApi("https://x-clients-be.onrender.com")

def test_get_emp():

    body=api.get_list_emp()
    assert len(body)>0

def test_get_active_emp():

    full_list=api.get_list_emp()
    filtered_list = api.get_list_emp(params_to_add={"isActive": "true"})
    assert len(full_list) >= len(filtered_list)


def test_add_emp():

    body=api.get_list_emp(params_to_add={'company': 14732})
    len_before=len(body)

    id=666
    firstName="Veronica" 
    lastName="Procopets" 
    middleName="Vadimovna" 
    companyId=14732
    email="VV@mail.ru"
    phone="86666666666"
    birthdate= "2024-07-22T11:10:27.947Z"
    

    result=api.create_emp(firstName, lastName, middleName, email, phone, id, companyId=companyId, birthdate=birthdate)
    assert result.status_code==201

    body=api.get_list_emp(params_to_add={'company': 14732})
    len_after=len(body)
    assert len_after-len_before==1
    assert body[-1]["firstName"]==firstName
    assert body[-1]["lastName"]==lastName

def test_edit_emp():

    body=api.get_list_emp(params_to_add={'company': 14732})
    len_before=len(body)

    id=666
    firstName="Veronica" 
    lastName="Procopets" 
    middleName="Vadimovna" 
    companyId=14732
    email="VV@mail.ru"
    phone="86666666666"
    birthdate= "2024-07-22T11:10:27.947Z"
    

    result=api.create_emp(firstName, lastName, middleName, email, phone, id, companyId=companyId, birthdate=birthdate)
    assert result.status_code==201
    id=result.json()["id"]
        
    new_lastName="Popova"
    new_email="newVV@mail.ru"
    new_phone="89996666666"
    
    edited=api.edit(id, new_lastName, new_phone, new_email)

    assert edited.status_code==200
    assert edited[phone]==new_phone
    assert edited[lastName]==new_lastName
    assert edited[email]==new_email
 #   assert edited[isActive]==isActive
