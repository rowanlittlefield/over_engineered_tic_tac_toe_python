import os
from app.board import Board
from app.controller import Controller

class Match():
  def __init__(self):
    self.board = Board()
  
  def play(self, controller: Controller) -> None:
    while self.board.game_over() is False:
      _clear_terminal()
      self.board.render()
      user_action = controller.get_input()
      self.board.handle_user_action(user_action)

def _clear_terminal() -> None:
  os.system('cls' if os.name == 'nt' else 'clear')
