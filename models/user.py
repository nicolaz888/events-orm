from sqlalchemy import Integer, Column, String

from config import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    company = Column(String(80), nullable=False)
