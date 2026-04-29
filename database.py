from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "postgresql://postgres:mysecretpassword@localhost:5432/postgres"

engine = create_engine(DB_URL)

Session = sessionmaker(bind=engine)

Base = declarative_base()