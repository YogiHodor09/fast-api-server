from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'


# Create SQLITE Engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False}
)

# To create DB Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for each DB Model
Base = declarative_base()
