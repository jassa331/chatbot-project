import pyodbc

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=188.40.211.2;"
    "DATABASE=db38045;"
    "UID=db38045;"
    "PWD=X%n3@4Wp7Pj+;"
    "Encrypt=no;"
)

def run_query(query: str):

    # remove ```sql markdown
    query = query.replace("```sql", "").replace("```", "").strip()

    print("SQL Query:", query)

    conn = pyodbc.connect(connection_string)

    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    return rows