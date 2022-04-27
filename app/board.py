from app.space import Space
from app.user_action import UserAction

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
    return False
  
  def handle_user_action(self, user_action: UserAction) -> None:
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
