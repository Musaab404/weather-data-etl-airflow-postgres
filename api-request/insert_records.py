from api_request import dummy_fetch_data
import psycopg2




def connect_to_db():
    print("Connecting to postgresql database...")
    # Simulate a database connection
    try:
        conn = psycopg2.connect(
                host="localhost", 
                port=5000,
                dbname="airflow",
                user="airflow",
                password="airflow")
        return conn
    except psycopg2.Eroor as e :
         print(f"database connection failed")
         raise


def create_table(conn):
    print("creating table if not exists")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT, 
                weather_descreptions TEXT, 
                wind_speed FLOAT, 
                time TIMESTAMP, 
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT
            );
        """)
        conn.commit()
        print("table was created")

    except psycopg2.Error as e:
        print(f"Failed to create table: {e}")
        raise





def insert_records(conn, data):
    print("inserting weather data into the databese")
    try:
        weather = data['current']
        location = data['location']
        cursor = conn.cursor()
        cursor.execute("""
                INSERT INTO dev.raw_weather_data(
                    city,
                    temperature,
                    weather_descreptions,
                    wind_speed,
                    time,
                    inserted_at,
                    utc_offset
                )VALUES (%s, %s, %s, %s, %s, NOW() , %s)
        
        
        """, (
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        )
            )
        conn.commit()
        print("data was inserted successfully")


    except psycopg2.Error as e:
        print(f"Failed to insert data: {e}")
        raise


def main():
    try:
        conn = connect_to_db()
        create_table(conn)
        data = dummy_fetch_data()
        insert_records(conn, data)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("database connection closed")






