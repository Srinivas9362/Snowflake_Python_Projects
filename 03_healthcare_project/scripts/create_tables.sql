use role accountadmin;

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
