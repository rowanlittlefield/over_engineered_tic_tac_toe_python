from dataclasses import dataclass

from app.game_state.match.space import Space

@dataclass
class BoardMemento():
  position: tuple[int, int]
  space: Space
  was_space_set: bool
