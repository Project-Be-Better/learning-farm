# region IMPORT
from pydantic import BaseModel
from typing import Optional

# endregion IMPORT


# class TodoModel(BaseModel):
#     title: str
#     desc: str


class TodoModel(BaseModel):
    title: str
    desc: Optional[str]  # Make 'desc' field optional
