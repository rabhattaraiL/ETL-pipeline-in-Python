from extract import extract_weather_data
from transform import transform_weather_data
from load import load_to_db


def run_etl():
    try:
        print('Starting ETL process')
        retrieved_data = extract_weather_data()
        transformed_data = transform_weather_data(retrieved_data)
        load_to_db(transformed_data, "weather_table_5day")
        print('ETL process complete')
    except Exception as e:
        print(f'Failed due to {e}')

if __name__ == "__main__":
    run_etl()
