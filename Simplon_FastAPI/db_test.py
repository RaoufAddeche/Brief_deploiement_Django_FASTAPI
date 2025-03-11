import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=raddechesqlserver.database.windows.net,1433;'
    'DATABASE=ussba;'
    'UID=raddecheadmin;'
    'PWD=Ussba2025rbx;'
    'Encrypt=yes;'
    'TrustServerCertificate=no;'
)

cursor = conn.cursor()
cursor.execute("SELECT @@VERSION;")
print(cursor.fetchone())

