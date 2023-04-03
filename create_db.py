import os
import inspect
import sqlite3
import datetime



def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
   
    """Creates the people table in the Social Network database"""
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS people (
                 id INTEGER PRIMARY KEY,
                 name TEXT,
                 age INTEGER,
                 id INTEGER,
                 address TEXT,
                 created_at TEXT,
                 updated_at TEXT)''')

    con.commit()
    con.close()

    return


def populate_people_table():
    """Populates the people table with 200 fake people"""
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()

    for i in range(200):

        generate_date=datetime.date.today().strftime("%Y-%m-%d")
        
        created_at = generate_date
        updated_at = generate_date

        cur.execute("INSERT  (created_at, updated_at) VALUES ( ?, ?)",
                  (created_at, updated_at))

    con.commit()
    con.close()
    return

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()

if __name__ == '__main__':
    main()
