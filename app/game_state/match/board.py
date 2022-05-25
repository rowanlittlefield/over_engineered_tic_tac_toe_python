from app.controller.user_action import UserAction
from app.game_state.match.board_memento import BoardMemento
from app.game_state.match.space import Space

class Board:
  def __init__(self):
    self.cursor_position = [0, 0]
    self.grid = [
        [Space.EMPTY, Space.EMPTY, Space.EMPTY],
        [Space.EMPTY, Space.EMPTY, Space.EMPTY],
        [Space.EMPTY, Space.EMPTY, Space.EMPTY],
    ]

  def render(self) -> None:
    for idx, row in enumerate(self.grid):
      row_values = []
      for jdx, space in enumerate(row):
        is_cursor_row = self.cursor_position[0] == idx and self.cursor_position[1] == jdx
        value = 'C' if is_cursor_row else space.value
        row_values.append(value)

      row_str = "|".join(row_values)
      print(row_str)
      if idx < len(self.grid) - 1:
        print("-----")
  
  def game_over(self) -> bool:
    if self._has_won(Space.X) or self._has_won(Space.O):
      return True
    
    flattened_grid = [item for sublist in self.grid for item in sublist]
    return all(element != Space.EMPTY for element in flattened_grid)

  def winner(self) -> Space | None:
    if self._has_won(Space.X):
      return Space.X
    elif self._has_won(Space.O):
      return Space.O
    
    return None

  def _has_won(self, space: Space) -> bool:
    has_won = False

    for row in self.grid:
      has_won = has_won or all(element == space for element in row)
    
    for i, _col in enumerate(self.grid[0]):
      column = []
      for _j, row in enumerate(self.grid):
        column.append(row[i])
      has_won = has_won or all(element == space for element in column)

    return has_won

  def move_cursor(self, user_action: UserAction) -> None:
    num_rows = len(self.grid)
    num_cols = len(self.grid[0])
    row, col = self.cursor_position
    
    match user_action:
      case UserAction.UP:
        self.cursor_position[0] = (row - 1) % num_rows
      case UserAction.RIGHT:
        self.cursor_position[1] = (col + 1) % num_cols
      case UserAction.DOWN:
        self.cursor_position[0] = (row + 1) % num_rows
      case UserAction.LEFT:
        self.cursor_position[1] = (col - 1) % num_cols
  
  def set_current_space(self, space) -> BoardMemento:
    was_space_set = False
    row, col = self.cursor_position
    if self.grid[row][col] == Space.EMPTY:
      self.grid[row][col] = space
      was_space_set = True

    return BoardMemento(
      position=(row, col),
      space=space,
      was_space_set=was_space_set
    )
  
  def undo(self, board_memento: BoardMemento) -> None:
    row, col = board_memento.position
    self.grid[row][col] = Space.EMPTY

  def redo(self, board_memento: BoardMemento) -> None:
    row, col = board_memento.position
    self.grid[row][col] = board_memento.space

