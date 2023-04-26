#!/usr/bin/python3
"""This is the state class"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String
from models.city import City

if getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """This is the class for State
        Attributes:
            name: input name
        """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City",
            cascade="all,delete-orphan",
            backref=backref("state", cascade="all"),
            passive_deletes=True,
            single_parent=True)

elif getenv("HBNB_TYPE_STORAGE") == "fs":
    class State(BaseModel, Base):
        """This is the class for State
        Attributes:
            name: input name
        """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)

        @property
        def cities(self):
            """returns list of City instances with state_id"""
            from models import storage
            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]
