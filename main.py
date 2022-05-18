from app.game import Game
from app.controller import Controller


def main() -> None:
  controller = Controller()
  game = Game(controller=controller)
  game.play()


if __name__ == "__main__":
  main()

