import os
from app.board import Board
from app.controller import Controller
from app.space import Space
from app.user_action import UserAction

class Match():
  def __init__(self):
    self.board = Board()
    self.current_player = Space.X
  
  def play(self, controller: Controller) -> None:
    while self.board.game_over() is False:
      _clear_terminal()
      self.board.render()
      user_action = controller.get_input()
      self._handle_user_action(user_action)

  def _handle_user_action(self, user_action) -> None:
    match user_action:
      case UserAction.ENTER:
        was_successful = self.board.set_current_space(self.current_player)
        if was_successful:
          self._toggle_current_user()
      case UserAction.UP|UserAction.RIGHT|UserAction.DOWN|UserAction.LEFT:
        self.board.move_cursor(user_action)

  
  def _toggle_current_user(self) -> None:
    if self.current_player == Space.X:
      self.current_player = Space.O
    else:
      self.current_player = Space.X

def _clear_terminal() -> None:
  os.system('cls' if os.name == 'nt' else 'clear')
