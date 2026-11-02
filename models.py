from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String, Boolean

class Base(DeclarativeBase): pass

class Task(Base):
    __tablename__ = "Tasks"

    id = Column(Integer, primary_key=True, index=True)
    taskName = Column(String, index=True)
    taskDescription = Column(String, nullable=True)
    isTaskDone = Column(Boolean, default=False)

