from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://tempuser:temppassword@localhost:3310/tempdatabase'
try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    connection = engine.connect()
    print("Connection successful!")
    connection.close()
except Exception as e:
    print(f"Error: {e}")