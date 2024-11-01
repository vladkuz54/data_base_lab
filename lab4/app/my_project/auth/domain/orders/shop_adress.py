from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Shop_Adress(db.Model, IDto):

    __tablename__ = 'shop_adress'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    street = db.Column(db.String(100), nullable=False)
    street_number = db.Column(db.Integer, nullable=False)
    gps_latitude = db.Column(db.Float, nullable=False)
    gps_longitude = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"Adress {self.id}, {self.street}, {self.street_number}, {self.gps_latitude}, {self.gps_longitude}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'street': self.street,
            'street_number': self.street_number,
            'gps_latitude': self.gps_latitude,
            'gps_longitude': self.gps_longitude
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Shop_Adress:
        obj = Shop_Adress(**dto_dict)
        return obj