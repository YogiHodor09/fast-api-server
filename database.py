from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# To connect to sqlite3 DB
# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'

# To connect to postgresql
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:root@localhost/TodoApplicationDatabase'

# To connect to mysql
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:root@127.0.0.1:3306/todoapp'


# Create SQLITE Engine
# engine = create_engine(
#     SQLALCHEMY_SQLITE_DATABASE_URL,
#     connect_args={'check_same_thread': False}
# )

# Create DB Engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# To create DB Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for each DB Model
Base = declarative_base()
