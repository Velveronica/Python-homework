
import allure
import requests
from datetime import datetime

@allure.epic("API сотрудники") 
@allure.severity("blocker")

class EmployeeApi:


    def __init__(self, url) -> None:

        self.url=url

    @allure.step("api. Получить список сотрудников компании через API")
    def get_list_emp(self, params_to_add=None):

        emp_list=requests.get(self.url+'/employee', params=params_to_add)
        return emp_list.json()

    @allure.step("api. Получить токен авторизации для пользователя {user}:{password}")
    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

    @allure.step("api. Создать сотрудника компании с {id}; {firstName}, {lastName}, {middleName}, {email}, {phone}, {id}, {isActive}, {url}, {companyId}, {birthdate}")
    def create_emp(self, firstName: str, 
                   lastName: str, 
                   middleName: str, 
                   email: str, 
                   phone: str, 
                   id: int, 
                   isActive: bool=True, 
                   url: str="", 
                   companyId: int="", 
                   birthdate: datetime=""):
        
        employee = {
        "id": id,
        "firstName": firstName,
        "lastName": lastName,
        "middleName": middleName,
        "companyId": companyId,
        "email": email,
        "url": url,
        "phone": phone,
        "birthdate": birthdate,
        "isActive": isActive
        }  
     
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee',json=employee, headers=my_headers)
        return resp

    @allure.step("api. Получить сотрудника по {id} сотрудника через API")
    def emp_id(self, id: int):
        resp = requests.get(self.url + f'/employee/{id}')
        return resp

    @allure.step("api. Отредактировать сотрудника компании с {id} через API {id}, {lastName}, {email}, {phone}, {isActive}, {url}")
    def edit(self, id: int, lastName: str, email: str, phone: str, isActive: bool=True, url: str=""):
        emp_editdata = {
            "lastName": lastName,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": isActive
    }
        my_headers = {"x-client-token": self.get_token()}
        resp = requests.patch(f"{self.url}/employee/{id}", headers=my_headers, json=emp_editdata)
        return resp