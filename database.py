from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# строка подключения
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# Создание движка
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}) # "check_same_thread": False - для подключения нескольких потоков

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)