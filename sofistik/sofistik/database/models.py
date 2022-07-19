import datetime

from sqlalchemy import (
    CHAR,
    DATETIME,
    INTEGER,
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Quads(Base):
    """Quad model for data base"""

    __tablename__ = 'quads'

    id = Column(Integer, primary_key=True)
    quad_number = Column(Integer, nullable=False, unique=True)
    node_0 = Column(String(255), nullable=False)
    node_1 = Column(String(255), nullable=False)
    node_2 = Column(String(255), nullable=False)
    node_3 = Column(String(255), nullable=False)
    area = Column(Integer, nullable=False)
    group = Column(Integer, nullable=False)
    bending_moment_mxx = Column(Integer, nullable=False)
    bending_moment_myy = Column(Integer, nullable=False)
    bending_moment_mxy = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Quad {self.quad_number}'
