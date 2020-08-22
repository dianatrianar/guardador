from datetime import date
import pandas as pd
from sqlalchemy import create_engine

today = date.today()

data = pd.Dataframe({
    "Fecha": today
    },index=[0])


data.to_csv(f"{today}.csv")

# string_conexion = "postgresql+psycopg2://postgres:LmKjxFyVxUvG6eWGClmz@database-test.crdvza4geaky.us-east-2.rds.amazonaws.com:5432/fechas"
#
# engine = create_engine(string_conexion)
#
# data.to_sql(name="date_tabla",con=engine,if_exist="append",index=False)
#engine.dispose()
