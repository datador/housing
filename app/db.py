import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Model(DeclarativeBase):
    metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    })

load_dotenv()

user = os.environ['HOUSING_USER']
password = os.environ['HOUSING_PASSWORD']
hostname = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
database = os.environ['POSTGRES_DB']
DATABASE_URL = f'postgresql+psycopg2://{user}:{password}@{hostname}:{port}/{database}'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(engine)