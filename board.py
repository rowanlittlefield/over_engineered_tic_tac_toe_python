from space import Space

class Board:
  def __init__(self):
    self.grid = [
        [Space.EMPTY, Space.EMPTY, Space.EMPTY],
        [Space.EMPTY, Space.EMPTY, Space.EMPTY],
        [Space.EMPTY, Space.EMPTY, Space.EMPTY],
    ]

  def render(self):
    for idx, row in enumerate(self.grid):
      row_values = map(lambda space: space.value, row)
      row_str = "|".join(row_values)
      print(row_str)
      if idx < len(self.grid) - 1:
        print("-----")