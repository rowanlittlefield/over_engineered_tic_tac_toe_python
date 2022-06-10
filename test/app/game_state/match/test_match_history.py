import json

from app.game_state.match.match_history import MatchHistory
from app.game_state.match.board_memento import BoardMemento
from app.game_state.match.space import Space

def test_to_json() -> None:
  previous_memento = BoardMemento(
      position=(0, 0),
      space=Space.X,
      was_space_set=True
  )
  previous = [previous_memento]
  later_memento = BoardMemento(
      position=(1, 1),
      space=Space.O,
      was_space_set=True
  )
  later = [later_memento]
  history = MatchHistory(previous=previous, later=later)
  history_dictionary = {
    "previous": [previous_memento.to_dict()],
    "later": [later_memento.to_dict()]
  }
  expected = json.dumps(history_dictionary)

  actual = history.to_json()

  assert actual == expected

def test_get_replay() -> None:
  previous_memento = BoardMemento(
    position=(0, 0),
    space=Space.X,
    was_space_set=True
  )
  previous = [previous_memento]
  history = MatchHistory(previous=previous)
  expected = previous

  actual = history.get_replay()

  assert actual == expected

def test_back_when_previous_is_not_empty() -> None:
  previous_memento = BoardMemento(
      position=(0, 0),
      space=Space.X,
      was_space_set=True
  )
  previous = [previous_memento]
  history = MatchHistory(previous=previous)
  expected = previous_memento

  actual = history.back()

  assert actual == expected

def test_back_when_previous_is_empty() -> None:
  history = MatchHistory()
  expected = None

  actual = history.back()

  assert actual == expected


def test_forward_when_later_is_not_empty() -> None:
  later_memento = BoardMemento(
      position=(1, 1),
      space=Space.O,
      was_space_set=True
  )
  later = [later_memento]
  history = MatchHistory(later=later)
  expected = later_memento

  actual = history.forward()

  assert actual == expected


def test_forward_when_later_is_empty() -> None:
  history = MatchHistory()
  expected = None

  actual = history.forward()

  assert actual == expected

def test_append_adds_new_memento() -> None:
  board_memento = BoardMemento(
    position=(1, 1),
    space=Space.O,
    was_space_set=True
  )
  history = MatchHistory()
  expected = board_memento

  history.append(board_memento=board_memento)

  actual = board_memento

  assert actual == expected

def test_append_clears_the_later_part_of_history():
  new_board_memento = BoardMemento(
    position=(1, 1),
    space=Space.O,
    was_space_set=True
  )
  later_memento = BoardMemento(
    position=(0, 0),
    space=Space.X,
    was_space_set=True
  )
  later = [later_memento]
  history = MatchHistory(later=later)
  expected = None

  history.append(board_memento=new_board_memento)

  actual = history.forward()

  assert actual == expected

