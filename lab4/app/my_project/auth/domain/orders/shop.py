from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Shop(db.Model, IDto):

    __tablename__ = 'shop'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)

    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    client = db.relationship('Client', backref='shops')

    shop_adress_id = db.Column(db.Integer, db.ForeignKey('shop_adress.id'), nullable=False)
    shop_adress = db.relationship('Shop_Adress', backref='shops')

    def __repr__(self) -> str:
        return f"Shop {self.id}, {self.client_id}, {self.shop_adress_id}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'client_id': self.client_id,
            'client': self.client.name,
            'shop_adress_id': self.shop_adress_id,
            'shop_street': self.shop_adress.street,
            'shop_street_number': self.shop_adress.street_number
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Shop:
        obj = Shop(**dto_dict)
        return obj