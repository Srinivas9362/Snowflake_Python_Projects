import requests
import snowflake.connector
from datetime import datetime
from config import (
    SF_USER, SF_PASSWORD, SF_ACCOUNT,
    SF_WAREHOUSE, SF_DATABASE, SF_SCHEMA,
    API_KEY
)
import json

def call_air_quality_api(city):
    url = f"https://api.api-ninjas.com/v1/airquality?city={city}"
    headers = {
        "X-Api-Key": API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json()

def load_raw_json_to_snowflake(api_data, city):
    conn = snowflake.connector.connect(
        user=SF_USER,
        password=SF_PASSWORD,
        account=SF_ACCOUNT,
        warehouse=SF_WAREHOUSE,
        database=SF_DATABASE,
        schema=SF_SCHEMA,
    )
    try:
        cur = conn.cursor()

        # Add city to JSON
        api_data['city'] = city

        # Convert dict to JSON string
        raw_json_str = json.dumps(api_data)

        # Use SELECT with TO_VARIANT to safely convert string to VARIANT
        # insert_sql = """
        #     INSERT INTO AIR_QUALITY_RAW (RAW_DATA, CITY, INGESTION_TIME)
        #     SELECT TO_VARIANT(%s), %s, %s
        # """
        # cur.execute(insert_sql, (raw_json_str, city, datetime.now()))

        insert_sql = """
            INSERT INTO AIR_QUALITY_RAW (RAW_DATA, CITY, INGESTION_TIME)
            SELECT TO_VARIANT(%s), %s, %s
        """
        cur.execute(insert_sql, (json.dumps(api_data), city, datetime.now()))


        print(f"Raw JSON inserted successfully for {city}.")
    except Exception as e:
        print("Error inserting into RAW table:", str(e))
    finally:
        cur.close()
        conn.close()


def main():
    cities = ["Delhi", "New York", "InvalidCity"]
    for city in cities:
        print(f"Calling API for: {city}")
        data = call_air_quality_api(city)
        print(f"API Response => {city}:", data)
        if "error" in data:
            print(f"Skipping {city}: {data['error']}")
            continue
        load_raw_json_to_snowflake(data,city)


if __name__ == "__main__":
    main()
