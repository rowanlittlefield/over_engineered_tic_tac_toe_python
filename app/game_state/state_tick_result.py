from dataclasses import dataclass, field

from app.game_state.state_status import StateStatus

@dataclass
class StateTickResult():
  status: StateStatus
  next_state: str = ''
  inputs: dict[str, str] = field(default_factory=dict)
