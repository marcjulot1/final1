from pathlib import Path
import json
import csv
import sqlite3
import pandas as pd


from api import result
Path('list.db').touch


def repository():
    conn = sqlite3.connect('list.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE quotes(quote_id int, quote text, author text)''')

    listdata = pd.read_csv('list.csv')
    listdata.to_sql('quotes', conn, if_exists='append', index=False)

    c.execute('''SELECT * FROM 'quotes''').fetchall()
