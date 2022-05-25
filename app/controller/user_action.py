from enum import Enum


class UserAction(Enum):
  ENTER = 'enter'
  UP = 'up'
  RIGHT = 'right'
  DOWN = 'down'
  LEFT = 'left'
  UNDO = 'undo'
  REDO = 'redo'
  NULL = ''
