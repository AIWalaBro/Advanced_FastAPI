from fastapi import FastAPI, HTTPException
from typing import List
from models import Employee

# employee db is an empty list.
# what it contains? - > list of employees
# varibale name : uska data type : aur uska value   ---> in this way you define your data type

employees_db = List[Employee] = []

app = FastAPI()

# Read all employees
@app.get("/employees", response_model = List[Employee])
def get_employees():
    return employees_db


# 2. Read specific employee
@app.get("/employees/{employee_id}", response_model = Employee)
def get_employee(employee_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == employee_id:
            return employees_db[index]
        
    raise HTTPException(status_code = 404, detail = f"Employee with id {employee_id} not found")


# 3. add the employee
@app.post("/employees", response_model = Employee)
def add_employee(new_employee: Employee):
    for employee in employees_db:
        if employee.id == new_employee.id:
            raise HTTPException(status_code = 400, detail = f"Employee with id {new_employee.id} already exists")
        employees_db.append(new_employee)
    return new_employee


# 4. update the employee
@app.put("/update_employees/{employee_id}", response_model = Employee)
def update_employee(employee_id: int, updated_employee: Employee):
    for index, employee in enumerate(employees_db):
        if employee.id == employee_id:
            employees_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code = 404, detail = f"Employee with id {employee_id} not found")


# 5. delete the employee
# which employee we want to delete i.e path parameter

@app.delete("/delete_employees/{employee_id}", response_model = Employee)
def delete_employee(employee_id: int):
    for index, employee in enumerate(employees_db):
        # check if employee id is present in the database
        if employee.id == employee_id:
            del employees_db[index]
            return {"message" : "employee deleted sucessfully"}
    raise HTTPException(status_code = 404, detail = "Employee not found")




