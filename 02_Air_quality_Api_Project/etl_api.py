import requests
import snowflake.connector
from datetime import datetime
from config import (
    SF_USER, SF_PASSWORD, SF_ACCOUNT,
    SF_WAREHOUSE, SF_DATABASE, SF_SCHEMA,
    API_KEY
)

def call_air_quality_api(city):
    url = f"https://api.api-ninjas.com/v1/airquality?city={city}"
    headers = {
        "X-Api-Key": API_KEY
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

def transform_data(city, api_response):
    aqi_value = api_response.get('overall_aqi')
    current_time = datetime.now()
    return (city, aqi_value, current_time)

def load_to_snowflake(record):
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
        insert_stmt = """
            INSERT INTO AIR_QUALITY (CITY, AQI, TIMESTAMP)
            VALUES (%s, %s, %s)
        """
        cur.execute(insert_stmt, record)
        print("Data inserted into Snowflake.")
    except Exception as e:
        print("Insert failed =>", str(e))
    finally:
        cur.close()
        conn.close()

# def main():
#     city_name = "Delhi"
#     api_data = call_air_quality_api(city_name)
#     print("API Response:", api_data)
#     record = transform_data(city_name, api_data)
#     load_to_snowflake(record)

def main():
    cities = ["Delhi", "New York", "Mumbai", "InvalidCity", "Karnataka"]

    for city_name in cities:
        print(f"\nProcessing city: {city_name}")
        api_data = call_air_quality_api(city_name)

        # If API returned an empty dict or None
        if not api_data or api_data.get('overall_aqi') is None:
            print(f"⚠️  AQI data not found for city '{city_name}'. Skipping.")
            continue

        record = transform_data(city_name, api_data)

        if record:
            load_to_snowflake(record)


if __name__ == "__main__":
    main()
