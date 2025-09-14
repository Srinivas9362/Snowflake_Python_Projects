# app/routers/patients.py
from fastapi import APIRouter, HTTPException
from app.db import get_connection
from app.models import Patient

router = APIRouter()   # <-- THIS IS REQUIRED

@router.post("/patients")
def add_patient(patient: Patient):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO patients (first_name, last_name, date_of_birth, gender)
            VALUES (%s, %s, %s, %s)
        """, (patient.first_name, patient.last_name, patient.date_of_birth, patient.gender))
        conn.commit()
        return {"message": "Patient added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/patients")
def get_patients(limit: int = 10):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT patient_id, first_name, last_name, gender FROM patients LIMIT {limit}")
        rows = cur.fetchall()
        return {"patients": rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
