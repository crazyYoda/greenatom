from datetime import datetime
from typing import List
from pydantic import BaseModel


class User(BaseModel):
    # id: int
    username: str


class UploadImage(BaseModel):

    title: str
    description: str
    tags: List[str]


class GetImage(BaseModel):
    user: User
    title: str
    description: str


class GetListImages(BaseModel):
    id: int
    file: str
    create_at: datetime




