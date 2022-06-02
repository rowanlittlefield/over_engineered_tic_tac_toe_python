import json
from typing import TypeVar, Type

from app.game_state.match.board_memento import BoardMemento

T = TypeVar('T', bound='MatchHistory')

class MatchHistory():
  def __init__(
    self,
    *,
    previous: list[BoardMemento]=[],
    later: list[BoardMemento]=[]
  ):
    self.previous = previous
    self.later = later

  @classmethod
  def from_json(cls: Type[T], json_history: str) -> T:
    history = json.loads(json_history)
    previous = [BoardMemento.from_dict(x) for x in history["previous"]]
    later = [BoardMemento.from_dict(x) for x in history["later"]]

    return cls(previous=previous, later=later)

  def get_replay(self):
    return self.previous.copy()

  def to_json(self) -> str:
    history = {
      "previous": [memento.to_dict() for memento in self.previous],
      "later": [memento.to_dict() for memento in self.later]
    }

    return json.dumps(history)

  def append(self, board_memento: BoardMemento):
    self.previous.append(board_memento)
    self.later.clear()

  def back(self) -> BoardMemento | None:
    if len(self.previous):
      board_memento = self.previous.pop() 
      self.later.append(board_memento)
      return board_memento

    return None

  def forward(self) -> BoardMemento | None:
    if len(self.later):
      board_memento = self.later.pop()
      self.previous.append(board_memento)
      return board_memento
    
    return None
