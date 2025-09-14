from fastapi import APIRouter, HTTPException
from app.db import get_connection
from app.models import Visit

router = APIRouter()

@router.post("/visits")
def add_visit(visit: Visit):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO visits (patient_id, visit_date, diagnosis, doctor_name)
            VALUES (%s, %s, %s, %s)
        """, (visit.patient_id, visit.visit_date, visit.diagnosis, visit.doctor_name))
        conn.commit()
        return {"message": "Visit recorded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/visits/{patient_id}")
def get_visits(patient_id: int):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"SELECT visit_id, visit_date, diagnosis, doctor_name FROM visits WHERE patient_id = {patient_id}")
        rows = cur.fetchall()
        return {"visits": rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
