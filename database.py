import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('case_queries.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            result TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_query(case_type, case_number, filing_year, result):
    conn = sqlite3.connect('case_queries.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO queries (case_type, case_number, filing_year, result, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (case_type, case_number, filing_year, str(result), datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()
