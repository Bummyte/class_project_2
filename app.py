from sqlalchemy import create_engine,text
connection_string= "mysql+mysqlconnector://root:bunmi123@localhost/user"
engine=create_engine(connection_string, echo=True)
with engine.connect() as connection:
    connection.execute(text("CREATE TABLE IF NOT EXIST biometrics(id INTEGER, name VARCHAR(50))"))
    connection.execute(text("INSERT INTO biometrics (id, name) VALUES (:id, :name)"), {"id": 1, "name":"John"}) 
    connection.execute(text("INSERT INTO biometrics (id, name) VALUES (:id, :name)"), [{"id": 2, "name":"Ben"},{"id":3, "name":"Paul"}])
    connection.commit()
