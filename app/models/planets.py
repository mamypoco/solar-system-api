from ..db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .moon import Moon

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    size: Mapped[str]
    moons: Mapped[list["Moon"]] = relationship(back_populates="planet")    

    def to_dict(self):
        return {
            "id": self.id, 
            "name": self.name, 
            "description": self.description,
            "size": self.size,
            # "moon": self.moon.name if self.moon_id else None
        }

    @classmethod # build a new instance when Planet.from_dict is called
    def from_dict(cls, planet_data):
        return cls(name=planet_data["name"], 
                description=planet_data["description"], 
                size=planet_data["size"],
                )
