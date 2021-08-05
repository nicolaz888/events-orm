from sqlalchemy import Column, Integer, String, Date, ForeignKey

from config import Base


class Event(Base):
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    date = Column(Date, nullable=False)
    attendees = Column(Integer, nullable=False, default=0)

    created_by = Column(Integer, ForeignKey('user.id'), nullable=False)
    type = Column(Integer, ForeignKey('event_type.id'), nullable=False)
