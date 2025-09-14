

healthcare_project/
│── app/                     # FastAPI app
│   ├── __init__.py
│   ├── main.py               # FastAPI entry point
│   ├── db.py                 # DB connection (Snowflake)
│   ├── models.py             # Pydantic models
│   ├── routers/              # API endpoints
│   │   ├── patients.py
│   │   └── visits.py
│
│── scripts/                  # ETL or setup scripts
│   └── create_tables.sql     # Snowflake table DDL
│
│── .env                      # Store credentials securely
│── requirements.txt          # Python dependencies
│── README.md



--step--01
<!-- Inside your project, create a virtual environment: -->
python -m venv venv
venv\Scripts\activate      # (Windows)


--step--02
<!-- Install dependencies: -->

pip install fastapi uvicorn snowflake-connector-python python-dotenv


--step--03

<!-- Add to requirements.txt: -->

fastapi
uvicorn
snowflake-connector-python
python-dotenv




<!-- Step 4: Snowflake Table Creation (Healthcare Domain) -->

In scripts/create_tables.sql:

CREATE OR REPLACE DATABASE healthcare_db;
CREATE OR REPLACE SCHEMA healthcare_schema;

-- Patient Master Table
CREATE OR REPLACE TABLE healthcare_db.healthcare_schema.patients (
    patient_id INT AUTOINCREMENT PRIMARY KEY,
    first_name STRING,
    last_name STRING,
    date_of_birth DATE,
    gender STRING,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Visit Records
CREATE OR REPLACE TABLE healthcare_db.healthcare_schema.visits (
    visit_id INT AUTOINCREMENT PRIMARY KEY,
    patient_id INT,
    visit_date DATE,
    diagnosis STRING,
    doctor_name STRING,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);


👉 Run this script in Snowflake Worksheet.