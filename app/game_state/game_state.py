from abc import ABC, abstractmethod
from typing import TypeVar, Type, Any

from app.controller.user_action import UserAction
from app.game_state.state_tick_result import StateTickResult

T = TypeVar('T', bound='GameState')

class GameState(ABC):

  @classmethod
  @abstractmethod
  def from_inputs(cls: Type[T], inputs: dict[str, Any]) -> T:
    pass
  
  @abstractmethod
  def render(self) -> None:
    pass

  @abstractmethod
  def play_tick(self, user_action: UserAction) -> StateTickResult:
    pass
