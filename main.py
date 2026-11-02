from fastapi import FastAPI, Depends, Body

from models import Base, Task
from database import engine, session_local

app = FastAPI()

# создаем таблицы
Base.metadata.create_all(bind=engine)

# Подключаемся к бд, и в любом случае, позже ее закрываем
def conn_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks")
def create_task(data  = Body(), db: Session = Depends(conn_db)):
    task = Task(taskName=data["name"], taskDescription=data["Description"])
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@app.get("/tasks")
def get_tasks(db: Session = Depends(conn_db)):
    return db.query(Task).all()


@app.get("/task")
def get_task(id, db: Session = Depends(conn_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if task == None:
        return JSONResponse(status_code=404, content={ "message": "Задача не найдена"})
    return task

@app.get("/")
def home_page():
    return {"message": "TO-DO list"}