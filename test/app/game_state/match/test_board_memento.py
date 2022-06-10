from app.game_state.match.board_memento import BoardMemento
from app.game_state.match.space import Space

def test_from_dict() -> None:
    dictionary = {
        "position": [0, 0],
        "space": "X",
        "was_space_set": True
    }
    expected = BoardMemento(
        position=(0, 0),
        space=Space.X,
        was_space_set=True
    )

    actual = BoardMemento.from_dict(dictionary)

    assert actual == expected

def test_to_dict() -> None:
  board_memento = BoardMemento(
    position=(0, 0),
    space=Space.X,
    was_space_set=True
  )
  expected = {
    "position": (0, 0),
    "space": "X",
    "was_space_set": True
  }

  actual = board_memento.to_dict()

  assert actual == expected