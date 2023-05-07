import pytest
from datetime import datetime
from postivo_app.positivo.repository import repository

pytestmark = pytest.mark.usefixtures("mappers")


def repository():
    conn = sqlite3.connect('list.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE quotes(quote_id int, quote text, author text)''')

    listdata = pd.read_csv('list.csv')
    listdata.to_sql('quotes', conn, if_exists='append', index=False)

    c.execute('''SELECT * FROM 'quotes''').fetchall()
