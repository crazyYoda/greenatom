import databases
import sqlalchemy
from sqlalchemy.orm import sessionmaker

metadata = sqlalchemy.MetaData()
database = databases.Database("postgresql://postgres:postgres@localhost/inbox")
engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost/inbox")


Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
