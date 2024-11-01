from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto

class Masters(db.Model, IDto):

    __tablename__ = 'masters'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    first_name = db.Column(db.String(60), nullable=False)
    patronymic = db.Column(db.String(60), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)

    def __repr__(self) -> str:
        return f"Masters {self.id}, {self.surname} {self.first_name} {self.patronymic}, {self.phone_number}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'surname': self.surname,
            'first_name': self.first_name,
            'patronymic': self.patronymic,
            'phone_number': self.phone_number
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Masters:
        obj = Masters(**dto_dict)
        return obj