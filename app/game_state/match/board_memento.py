from dataclasses import dataclass
from typing import TypeVar, Type, Any

from app.game_state.match.space import Space

T = TypeVar('T', bound='BoardMemento')

@dataclass
class BoardMemento():
  position: tuple[int, int]
  space: Space
  was_space_set: bool

  @classmethod
  def from_dict(cls: Type[T], history_dict: dict[str, Any]):
    position = (history_dict["position"][0], history_dict["position"][1])
    
    return cls(
        position=position,
        space=Space[history_dict["space"]],
        was_space_set=history_dict["was_space_set"]
    )

  def to_dict(self):
    return {
      "position": self.position,
      "space": self.space.value,
      "was_space_set": self.was_space_set
    }
