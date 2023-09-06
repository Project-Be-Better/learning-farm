# region IMPORT
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from database import fetch_all_todos, fetch_one_todo, create_todo, update_todo, remove_todo
from model import TodoModel
from fastapi.exceptions import HTTPException

# endregion IMPORT

load_dotenv()

PORT = os.environ.get("PORT")
app = FastAPI()

origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": PORT}


@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response


@app.get("/api/todo/{title}", response_model=TodoModel)
async def get_todo_by_id(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")


@app.post("/api/todo", response_model=TodoModel)
async def post_todo(todo: TodoModel):
    response = await create_todo(dict(todo))
    if response:
        return response
    raise HTTPException(400, f"Something went wrong while trying to create todo")


@app.put("/api/todo/{title}", response_model=TodoModel)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")


@app.delete("/api/todo/{title}")
async def delete_todo(title: str):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {title}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
