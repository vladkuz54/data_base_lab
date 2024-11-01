from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto

class ServiceType(db.Model, IDto):

    __tablename__ = 'service_type'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"ServiceType {self.id}, {self.name}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'name': self.name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ServiceType:
        obj = ServiceType(**dto_dict)
        return obj