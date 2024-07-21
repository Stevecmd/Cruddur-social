#!/usr/bin/env python3
import psycopg
import os
import sys

connection_url = os.getenv("CONNECTION_URL")

if not connection_url:
    print("Error: CONNECTION_URL environment variable is not set.")
    sys.exit(1)

conn = None
try:
    print('Attempting connection...')
    conn = psycopg.connect(connection_url)
    print("Connection successful!")
except psycopg.Error as e:
    print("Unable to connect to the database:", e)
finally:
    if conn is not None:
        conn.close()
    else:
        print("No connection to close.")
