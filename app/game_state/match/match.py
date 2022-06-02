import os
from time import sleep
from typing import TypeVar, Type, Any

from app.game_state.match.board import Board
from app.game_state.game_state import GameState
from app.game_state.match.match_history import MatchHistory
from app.game_state.match.space import Space
from app.game_state.state_tick_result import StateTickResult
from app.game_state.state_status import StateStatus
from app.controller.user_action import UserAction

T = TypeVar('T', bound='Match')
class Match(GameState):
  GAME_SAVE_FILE_RELATIVE_LOCATION = "game_saves/save_state.json"
  
  def __init__(
    self,
    *,
    board: Board=Board(),
    current_player: Space=Space.X,
    history: MatchHistory=MatchHistory()
  ):
    self.board = board
    self.current_player = current_player
    self.history = history

  @classmethod
  def from_inputs(cls: Type[T], inputs: dict[str, Any]) -> T:
    if inputs.get("should_load_game", False):
      return cls.load_match()

    return cls()
  
  @classmethod
  def load_match(cls: Type[T]) -> T:
    save_file_path = os.path.join(os.getcwd(), cls.GAME_SAVE_FILE_RELATIVE_LOCATION)
    with open(save_file_path, 'r') as save_file:
      history_json = save_file.read()

    match_history = MatchHistory.from_json(history_json)
    replay = match_history.get_replay()
    board = Board()

    for board_memento in replay:
      board.redo(board_memento)

    last_set_space = replay[-1].space
    if last_set_space == Space.X:
      current_player = Space.O
    else:
      current_player = Space.X
    
    return Match(
      board=board,
      current_player=current_player,
      history=match_history
    ) 

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
        board_memento = self.board.set_current_space(self.current_player)

        if board_memento.was_space_set:
          self.history.append(board_memento)
          self._toggle_current_user()
      case UserAction.UP|UserAction.RIGHT|UserAction.DOWN|UserAction.LEFT:
        self.board.move_cursor(user_action)
      case UserAction.UNDO:
        board_memento = self.history.back()

        if board_memento:
          self.board.undo(board_memento)
          self._toggle_current_user()
      case UserAction.REDO:
        board_memento = self.history.forward()

        if board_memento:
          self.board.redo(board_memento)
          self._toggle_current_user()
      case UserAction.SAVE:
        self._save_match()
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
  
  def _save_match(self):
    history_json = self.history.to_json()
    save_file_path = os.path.join(os.getcwd(), Match.GAME_SAVE_FILE_RELATIVE_LOCATION)
    
    with open(save_file_path, 'w') as save_file:
      save_file.write(history_json)
