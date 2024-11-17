import uuid
from app.models.__init__ import BaseModel
from datetime import datetime


class Amenity(BaseModel):
    def __init__(self, name):
        if not name or len(name) > 50:
            raise ValueError("Amenity name is required and must be maximum 50 characters long.")
        self.name = name
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def save(self):
        self.updated_at = datetime.now()


    def dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }