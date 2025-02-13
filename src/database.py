import os
import json
import psycopg2
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}

def create_tables():
    """Initialize database tables."""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    with open("sql_schemas/schema.sql") as f:
        cur.execute(f.read())
    conn.commit()
    cur.close()
    conn.close()

def store_form(json_path):
    """Store JSON data in the database."""
    with open(json_path) as f:
        form_data = json.load(f)
    
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    cur.execute("""
    INSERT INTO forms_data (patient_id, form_json)
    VALUES (%s, %s)
    """, (1, json.dumps(form_data)))  # Replace with actual patient ID logic
    
    conn.commit()
    cur.close()
    conn.close()
    print("Data successfully stored in database")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--store", required=True, help="Path to JSON file")
    args = parser.parse_args()
    store_form(args.store)