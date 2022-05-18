from abc import ABC, abstractmethod

from app.user_action import UserAction
from app.state_tick_result import StateTickResult

class GameState(ABC):
  
  @abstractmethod
  def render(self) -> None:
    pass

  @abstractmethod
  def play_tick(self, user_action: UserAction) -> StateTickResult:
    pass
