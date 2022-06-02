from typing import TypeVar, Type, Any

from app.game_state.game_state import GameState
from app.controller.user_action import UserAction
from app.game_state.state_status import StateStatus
from app.game_state.state_tick_result import StateTickResult
from app.controller.user_action import UserAction

T = TypeVar('T', bound='MainMenu')
class MainMenu(GameState):
  NEW_GAME = 'New Game'
  LOAD_GAME = 'Load Game'
  WINDOW_OPTIONS = [
    NEW_GAME,
    LOAD_GAME
  ]
  
  def __init__(self):
    self.window_index = 0
  
  @classmethod
  def from_inputs(cls: Type[T], inputs: dict[str, Any]) -> T:
    return cls()
  
  def play_tick(self, user_action: UserAction) -> StateTickResult:
    match user_action:
      case UserAction.UP:
        self.window_index = (self.window_index - 1) % len(MainMenu.WINDOW_OPTIONS)
        return StateTickResult(status=StateStatus.IN_PROGRESS)
      case UserAction.DOWN:
        self.window_index = (self.window_index + 1) % len(MainMenu.WINDOW_OPTIONS)
        return StateTickResult(status=StateStatus.IN_PROGRESS)
      case UserAction.ENTER:
        return self._handle_enter()
      case _:
        return StateTickResult(status=StateStatus.IN_PROGRESS)
    
  
  def _handle_enter(self) -> StateTickResult:
    selected_window_option = MainMenu.WINDOW_OPTIONS[self.window_index]
    
    match selected_window_option:
      case MainMenu.NEW_GAME:
        inputs = {"should_load_game": False }
        
        return StateTickResult(
          inputs=inputs,
          status=StateStatus.COMPLETED,
          next_state="match"
        )
      case MainMenu.LOAD_GAME:
        inputs = { "should_load_game": True }

        return StateTickResult(
          inputs=inputs,
          status=StateStatus.COMPLETED,
          next_state="match"
        )
      case _:
        return StateTickResult(status=StateStatus.IN_PROGRESS)

  def render(self) -> None:
    print("Main Menu")
    print("")

    for idx, option in enumerate(MainMenu.WINDOW_OPTIONS):
      if idx == self.window_index:
        print(f"{option} <")
      else:
        print(option)