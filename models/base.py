from sqlalchemy.orm import DeclarativeBase

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from datetime import datetime
from extensions import db
class Base (db.Model):
    __abstract__ = True

class BaseIncr (Base):
    __abstract__ = True
    loid = Column(Integer, primary_key=True, autoincrement=True)

class TimeStampedModel (BaseIncr):
    __abstract__ = True
    create_time = Column(DateTime, default=func.utc_timestamp())
    update_time = Column(DateTime, onupdate=func.utc_timestamp())
