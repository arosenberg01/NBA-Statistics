from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql+psycopg2://arosenberg@localhost/nba_py', echo=True)
Session = sessionmaker(bind=engine)
# sqllite_engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

class Event_Id(Base):
    __tablename__ = 'event_dates'

    id = Column(Integer, primary_key=True)
    event_id = Column(String)

# Base.metadata.create_all(engine)

# Base.metadata.create_all(sqllite_engine)

fake_event_id = Event_Id(event_id="test_id_for_game!")

session = Session()

session.add(fake_event_id)
session.commit()

print(fake_event_id.id)
