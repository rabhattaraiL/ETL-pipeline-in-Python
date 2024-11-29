import psycopg2
from psycopg2.extras import execute_values
from config import DB_CONFIG

def load_to_db(transformed_data, db_table_name):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        insert_query = f""" 
            INSERT INTO {db_table_name} 
            (datetime, temperature, human_temp_feel, min_temp, max_temp, pressure, humidity, wind_speed)
            VALUES %s;
        """
        data_tuples = transformed_data.to_records(index=False).tolist()
        execute_values(cursor, insert_query, data_tuples)
        conn.commit()
        print(f'Data sucessfully loaded into table: {db_table_name}')
    except Exception as e:
        print(f"Failed to load data: {e}")
    finally:
        cursor.close()
        conn.close()