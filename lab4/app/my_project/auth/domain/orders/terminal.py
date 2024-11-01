from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Terminal(db.Model, IDto):

    __tablename__ = 'terminal'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    shop = db.relationship('Shop', backref='terminals')
    manufactures_id = db.Column(db.Integer, db.ForeignKey('manufactures.id'), nullable=False)
    manufactures = db.relationship('Manufactures', backref='terminals')
    date_explotation = db.Column(db.Date, nullable=False)

    def __repr__(self) -> str:
        return f"Terminal {self.id}, {self.shop_id}, {self.manufactures_id}, {self.date_explotation}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'shop_id': self.shop_id,
            'manufactures_id': self.manufactures_id,
            'manufacturer': self.manufactures.name,
            'date_explotation': self.date_explotation.strftime('%Y-%m-%d')  # Format date without time
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Terminal:
        obj = Terminal(**dto_dict)
        return obj