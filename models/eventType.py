from sqlalchemy import Integer, Column, String

from config import Base


class EventType(Base):
    __tablename__ = 'event_type'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
