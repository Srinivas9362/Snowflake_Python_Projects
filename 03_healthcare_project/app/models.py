from pydantic import BaseModel
from datetime import date

class Patient(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str

class Visit(BaseModel):
    patient_id: int
    visit_date: date
    diagnosis: str
    doctor_name: str
