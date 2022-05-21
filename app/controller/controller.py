from app.controller.user_action import UserAction

class Controller():
  def get_input(self) -> UserAction:
    user_input = input("Enter your value:")
    user_action = self._map_to_user_action(user_input)
    return user_action

  def _map_to_user_action(self, user_input) -> UserAction:
    match user_input:
      case 'f':
        return UserAction.ENTER
      case 'w':
        return UserAction.UP
      case 'd':
        return UserAction.RIGHT
      case 's':
        return UserAction.DOWN
      case 'a':
        return UserAction.LEFT
      case _:
        return UserAction.NULL