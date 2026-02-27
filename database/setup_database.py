import sqlite3
import os

def setup_database():
    """Create the database and tables if they don't already exist"""

    # Create the database folder if it doesn't exist.
    os.makedirs('database', exist_ok=True)

    conn = sqlite3.connect('database/it-dashboard.db')
    cursor = conn.cursor()

    # Create ping_results table
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS ping_results (
                    id        INTEGER PRIMARY KEY AUTOINCREMENT,
                    ip_address TEXT NOT NULL,
                    port INTEGER NOT NULL,
                    status TEXT NOT NULL,
                    timestamp TEXT NOT NULL
                    )
                ''')
    
    # Create port_results table
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS port_results (
                    id        INTEGER PRIMARY KEY AUTOINCREMENT,
                    ip_address TEXT NOT NULL,
                    port INTEGER NOT NULL,
                    status TEXT NOT NULL,
                    timestamp TEXT NOT NULL
                )
            ''')
    
    conn.commit()
    conn.close()

    print('Database setup complete.')
    print('Tables created: ping_results, port_results')


setup_database()