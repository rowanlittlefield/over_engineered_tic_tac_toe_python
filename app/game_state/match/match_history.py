from app.game_state.match.board_memento import BoardMemento

class MatchHistory():
  def __init__(self):
    self.previous = []
    self.later = []

  def append(self, board_memento: BoardMemento):
    self.previous.append(board_memento)
    self.later.clear()

  def back(self) -> BoardMemento | None:
    if len(self.previous):
      board_memento = self.previous.pop() 
      self.later.append(board_memento)
      return board_memento

    return None

  def forward(self) -> BoardMemento | None:
    if len(self.later):
      board_memento = self.later.pop()
      self.previous.append(board_memento)
      return board_memento
    
    return None
