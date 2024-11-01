from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Invoices(db.Model, IDto):

    __tablename__ = 'invoices'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    service_job_id = db.Column(db.Integer, db.ForeignKey('service_job.id'), nullable=False)
    service_job = db.relationship('ServiceJob', backref='invoices')
    date = db.Column(db.Date, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return f"Invoice {self.id}, {self.service_job_id}, {self.date}, {self.total_price}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'service_job_id': self.service_job_id,
            'service_job_name': self.service_job.service_type.name,
            'date': self.date.strftime('%Y-%m-%d')
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Invoices:
        obj = Invoices(**dto_dict)
        return obj