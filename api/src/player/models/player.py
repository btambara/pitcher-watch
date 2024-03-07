from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    mlb_id = Column(Integer, unique=True)
    full_name = Column(String)
    primary_number = Column(Integer)
    current_team_id = Column(Integer)
    primary_position_code = Column(String)
    stats = relationship("Stats", back_populates="player")
    pitches = relationship("Pitches", back_populates="player")


class Stats(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True)
    mlb_id = Column(Integer, ForeignKey("players.mlb_id"))
    player = relationship("Player", back_populates="stats")
    season = Column(Integer)
    team_id = Column(Integer)
    stats = Column(JSONB)


class Pitches(Base):
    __tablename__ = "pitches"

    id = Column(Integer, primary_key=True)
    mlb_id = Column(Integer, ForeignKey("players.mlb_id"))
    player = relationship("Player", back_populates="pitches")
    season = Column(Integer)
    team_id = Column(Integer)
    pitches = Column(JSONB)
