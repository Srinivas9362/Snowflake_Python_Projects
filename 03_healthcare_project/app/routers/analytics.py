from fastapi import APIRouter, HTTPException
from app.db import get_connection

router = APIRouter()

@router.get("/analytics/top-diagnoses")
def top_diagnoses(limit: int = 5):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"""
            SELECT diagnosis, COUNT(*) as visit_count
            FROM visits
            GROUP BY diagnosis
            ORDER BY visit_count DESC
            LIMIT {limit}
        """)
        rows = cur.fetchall()
        return {"top_diagnoses": rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
