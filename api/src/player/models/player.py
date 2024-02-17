from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    mlb_id = Column(Integer)
    full_name = Column(String)
    primary_number = Column(Integer)
    current_team_id = Column(Integer)
    primary_position_code = Column(String)
