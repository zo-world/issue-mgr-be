from flask import (
    Flask,
    request
)

from app.database import task

app = Flask(__name__)

@app.get("/")
@app.get('/ping')
def ping():
    out = {
      "ok": True,
      "message": "pong"
    }
    return out

@app.get('/tasks')
def get_all_tasks():
    task_list = task.scan()
    out = {
      "ok": True,
      "tasks": task_list
    }
    return out

@app.get('/tasks/<int:pk>')
def get_task_by_id(pk):
    mytask = task.select_by_id(pk)
    out = {
        "ok": True,
        "task": mytask
    }
    return out

@app.post('/tasks')
def create_task():
    raw_data = request.json
    task.insert(raw_data)
    return "", 204

@app.put('/tasks/<int:pk>')
def update_task(pk):
    raw_data = request.json
    task.update(raw_data, pk)
    return "", 204

@app.post('/tasks/<int:pk>')
def delete_task(pk):
    task.delete(pk)
    return "", 204