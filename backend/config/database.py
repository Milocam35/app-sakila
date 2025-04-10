import os

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sshtunnel import SSHTunnelForwarder # type: ignore
import pymysql # type: ignore
from urllib.parse import quote_plus

# Configuración del túnel
tunnel = SSHTunnelForwarder(
    ('ec2-54-89-229-108.compute-1.amazonaws.com', 22),
    ssh_username='ubuntu',
    ssh_pkey = r"C:\Users\Camilo\Downloads\labsuser (1).pem",
    remote_bind_address=('database-1.c0dntp3bsb6x.us-east-1.rds.amazonaws.com', 3306)
)
tunnel.start()

password = quote_plus("Cm558169#")
DB_URL = f"mysql+pymysql://admin:{password}@localhost:{tunnel.local_bind_port}/sakila"
engine = create_engine(DB_URL)

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()