from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Client(db.Model, IDto):

    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)

    def __repr__(self) -> str:
        return f"Client({self.id}, '{self.name}', '{self.number}', '{self.client_type}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Client:
        obj = Client(**dto_dict)
        return obj
