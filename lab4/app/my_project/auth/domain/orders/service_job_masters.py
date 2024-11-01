from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class ServiceJobMasters(db.Model, IDto):
    __tablename__ = 'service_job_masters'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    service_job_id = db.Column(db.Integer, db.ForeignKey('service_job.id'), nullable=False)
    service_job = db.relationship('ServiceJob', backref='service_job_masters')
    master_id = db.Column(db.Integer, db.ForeignKey('masters.id'), nullable=False)
    master = db.relationship('Masters', backref='service_job_masters')

    def __repr__(self) -> str:
        return f"ServiceJobMasters {self.id} {self.service_job_id} {self.master_id}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'service_job_id': self.service_job_id,
            'master_id': self.master_id,
            'master_surname': self.master.surname,
            'master_phone': self.master.phone_number
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ServiceJobMasters:
        obj = ServiceJobMasters(**dto_dict)
        return obj
