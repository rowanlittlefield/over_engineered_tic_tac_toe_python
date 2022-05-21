from abc import ABC, abstractmethod

from app.controller.user_action import UserAction
from app.game_state.state_tick_result import StateTickResult

class GameState(ABC):
  
  @abstractmethod
  def render(self) -> None:
    pass

  @abstractmethod
  def play_tick(self, user_action: UserAction) -> StateTickResult:
    pass
