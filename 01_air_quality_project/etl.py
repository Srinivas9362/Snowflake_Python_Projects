import snowflake.connector
from datetime import datetime

def load_to_snowflake(city, aqi_value):
    conn = snowflake.connector.connect(
        user='Srinvisu83278',
        password='Sjbrbhrkgen@878797',
        account='uou9-97879',
        warehouse='COMPUTE_WH',
        database='DEMO_DB',
        schema='PUBLIC'
    )

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
    load_to_snowflake("Delhi", 150)
    load_to_snowflake("Karnataka", 400)
    load_to_snowflake("Andra", 15000)
    load_to_snowflake("Kerala", 159790)
