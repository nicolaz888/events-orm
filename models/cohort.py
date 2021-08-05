from sqlalchemy import Column, Integer, String

from config import Base


class Cohort(Base):
    __tablename__ = 'cohort'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
