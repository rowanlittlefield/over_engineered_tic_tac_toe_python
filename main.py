from app.match import Match
from app.controller import Controller

def main():
  controller = Controller()
  match = Match()
  match.play(controller)


if __name__ == "__main__":
  main()

