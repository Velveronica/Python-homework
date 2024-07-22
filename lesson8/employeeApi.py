
import requests

class EmployeeApi:

    def __init__(self, url) -> None:
        
        self.url=url

    def get_list_emp(self, params_to_add=None):

        emp_list=requests.get(self.url+'/employee', params=params_to_add)
        return emp_list.json()
    
    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    
    def create_emp(self, firstName, lastName, middleName, email, phone, id, isActive=True, url="", companyId="", birthdate=""):
        
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
    
    def emp_id(self, id):

        resp = requests.get(self.url + '/employee'+str(id))
        return resp
    
    def edit(self, id, lastName, email, phone, isActive=True, url=""):

        emp_editdata={
        "lastName": lastName,
        "email": email,
        "url": url,
        "phone": phone,
        "isActive": True
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + f"/employee/{id}", headers=my_headers, json=emp_editdata)
        return resp



