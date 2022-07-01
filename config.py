from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASSWORD"]
host = os.environ["MYSQL_HOST"]
database = os.environ["MYSQL_DATABASE"]

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'
print(DATABASE_CONNECTION_URI)

engine = create_engine(DATABASE_CONNECTION_URI, pool_size=100, max_overflow=0)
