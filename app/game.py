import os

from app.controller.controller import Controller
from app.game_state.main_menu.main_menu import MainMenu
from app.game_state.match.match import Match
from app.game_state.state_status import StateStatus

class Game():
  STATE_MAP = {
    "match": Match,
    "main_menu": MainMenu
  }

  def __init__(self, *, controller=Controller()):
    self.state = MainMenu()
    self.controller = controller
  
  def play(self) -> None:
    while True:
      self._play_tick()


  def _play_tick(self) -> None:
    self._render()
    user_action = self.controller.get_input()
    state_tick_result = self.state.play_tick(user_action)

    match state_tick_result.status:
      case StateStatus.COMPLETED:
        self._state_transition(
          next_state=state_tick_result.next_state
        )
      case _:
        pass

  def _render(self) -> None:
    _clear_terminal()
    self.state.render()
    print("")
  
  def _state_transition(self, *, next_state: str) -> None:
    next_state_cls = Game.STATE_MAP[next_state]
    self.state = next_state_cls()


def _clear_terminal() -> None:
  os.system('cls' if os.name == 'nt' else 'clear')
