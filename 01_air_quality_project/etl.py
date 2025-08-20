import snowflake.connector
from datetime import datetime
from config import SF_USER, SF_PASSWORD, SF_ACCOUNT, SF_WAREHOUSE, SF_DATABASE, SF_SCHEMA

def load_to_snowflake(city, aqi_value):
    conn = snowflake.connector.connect(
        user=SF_USER,
        password=SF_PASSWORD,
        account=SF_ACCOUNT,
        warehouse=SF_WAREHOUSE,
        database=SF_DATABASE,
        schema=SF_SCHEMA,
    )
    # Rest of your insert code...


    try:
        cur = conn.cursor()
        current_time = datetime.now()
        insert_sql = """
            INSERT INTO AIR_QUALITY (CITY, AQI, TIMESTAMP)
            VALUES (%s, %s, %s)
        """
        cur.execute(insert_sql, (city, aqi_value, current_time))
        print("Data inserted successfully.")
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    load_to_snowflake("New_york", 150)
    load_to_snowflake("Germany", 400)
    load_to_snowflake("India", 15000)
    load_to_snowflake("Japan", 159790)
