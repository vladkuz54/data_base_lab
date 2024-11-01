from __future__ import annotations
from typing import Dict, Any
from datetime import datetime, timedelta

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class ServiceJob(db.Model, IDto):
    __tablename__ = 'service_job'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    terminal_id = db.Column(db.Integer, db.ForeignKey('terminal.id'), nullable=False)
    terminal = db.relationship('Terminal', backref='service_jobs')
    service_type_id = db.Column(db.Integer, db.ForeignKey('service_type.id'), nullable=False)
    service_type = db.relationship('ServiceType', backref='service_jobs')
    time_start = db.Column(db.DateTime, nullable=False)
    time_end = db.Column(db.DateTime, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f"Terminal {self.id}, {self.terminal_id}, {self.service_type_id}, {self.time_start}, {self.time_end}, {self.date}"

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'terminal_id': self.terminal_id,
            'service_type_id': self.service_type_id,
            'service_type': self.service_type.name,
            'time_start': self.format_time(self.time_start),
            'time_end': self.format_time(self.time_end),
            'date': self.date.strftime('%Y-%m-%d')
        }

    @staticmethod
    def format_time(time_value: datetime) -> str:
        if isinstance(time_value, datetime):
            return time_value.strftime('%H:%M:%S')
        elif isinstance(time_value, timedelta):
            total_seconds = int(time_value.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{hours:02}:{minutes:02}:{seconds:02}"
        return str(time_value)

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ServiceJob:
        obj = ServiceJob(**dto_dict)
        return obj
