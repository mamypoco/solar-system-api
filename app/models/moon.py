from ..db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, TYPE_CHECKING
from sqlalchemy import ForeignKey

if TYPE_CHECKING:
    from .planets import Planet

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    size: Mapped[str]
    description: Mapped[str]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped["Planet"] = relationship(back_populates="moons")

    def to_dict(self):
        result = {
            "id": self.id,
            "size": self.size,
            "description": self.description
        }
        if self.planet_id:
            result.update({
                "planet_id": self.planet_id,
                "planet": self.planet.name
            })

        return result
    
    @classmethod
    def from_dict(cls, moon_data):
        
        new_moon = cls(
            size=moon_data["size"],
            description=moon_data["description"],
            planet_id=moon_data.get("planet_id", None)
        )

        return new_moon