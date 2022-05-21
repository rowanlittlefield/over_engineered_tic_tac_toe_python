from time import sleep

from app.game_state.match.board import Board
from app.game_state.game_state import GameState
from app.game_state.match.space import Space
from app.game_state.state_tick_result import StateTickResult
from app.game_state.state_status import StateStatus
from app.controller.user_action import UserAction

class Match(GameState):
  def __init__(self):
    self.board = Board()
    self.current_player = Space.X

  def render(self) -> None:
    self.board.render()

  def play_tick(self, user_action: UserAction) -> StateTickResult:
    self._handle_user_action(user_action)

    if self.board.game_over():
      self._render_game_over_message()

      return StateTickResult(
        status=StateStatus.COMPLETED,
        next_state="main_menu"
      )

    return StateTickResult(status=StateStatus.IN_PROGRESS)

  def _handle_user_action(self, user_action: UserAction) -> None:
    match user_action:
      case UserAction.ENTER:
        was_successful = self.board.set_current_space(self.current_player)
        if was_successful:
          self._toggle_current_user()
      case UserAction.UP|UserAction.RIGHT|UserAction.DOWN|UserAction.LEFT:
        self.board.move_cursor(user_action)
      case _:
        pass

  
  def _toggle_current_user(self) -> None:
    if self.current_player == Space.X:
      self.current_player = Space.O
    else:
      self.current_player = Space.X
  
  def _render_game_over_message(self) -> None:
    print("Game Over!")
    winner = self.board.winner()
    
    game_over_message = "Draw!"
    if winner:
      game_over_message = f"Winner is {winner.value}"

    print(game_over_message)
    sleep(5)
