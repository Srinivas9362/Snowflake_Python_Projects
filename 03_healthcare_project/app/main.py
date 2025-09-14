from fastapi import FastAPI
from app.routers import patients, visits
from app.routers import analytics



app = FastAPI(title="Healthcare Data API")


app.include_router(patients.router)
app.include_router(visits.router)
app.include_router(analytics.router)

@app.get("/")
def root():
    return {"message": "Healthcare FastAPI + Snowflake Project Running"}

