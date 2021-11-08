import datetime
from typing import Optional

import ormar

from DB.db import metadata, database


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=50, unique=True)
    password_hash: str = ormar.String(max_length=100, nullable=True)


class Image(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    file: str = ormar.String(max_length=1000)
    create_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
    user: Optional[User] = ormar.ForeignKey(User)
