# region IMPORT
from model import TodoModel
import motor.motor_asyncio  # MongoDB Driver

# endregion IMPORT

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.TodoList
collection = database.todo


async def fetch_one_todo(title):
    """Fetch one Todo from the database"""

    document = await collection.find_one({"title": title})
    return document


async def fetch_all_todos():
    """Fetch all the todos in the database"""

    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(TodoModel(**document))
    return todos


async def create_todo(todo):
    """Insert a new todo into the database"""

    document = todo
    result = await collection.insert_one(document)
    created_todo = await collection.find_one({"_id": result.inserted_id})
    return created_todo


async def update_todo(title, desc):
    """Update a todo in the database"""

    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document


async def remove_todo(title):
    """Delete a todo from the database"""

    await collection.delete_one({"title": title})
    return True
