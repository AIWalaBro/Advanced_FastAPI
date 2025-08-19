# we define all the schema with the help of pydantic"

from typing import Optional
from pydantic import BaseModel, EmailStr

class EmployeeBase(BaseModel):
    name : str
    email : str
    
    
class EmployeeCreate(EmployeeBase):
    # while creating new email it will overright the baseclass email
    email : Optional[EmailStr]
    

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id : int
    
    class Config:
        orm_mode: True