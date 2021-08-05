from sqlalchemy.orm import sessionmaker

from config import engine, Base
from models.event import Event
from models.user import User
from models.eventType import EventType
from models.campus import Campus
from models.cohort import Cohort

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    print(session.query(User).filter_by(name='nicolaz'))

    session.close()
