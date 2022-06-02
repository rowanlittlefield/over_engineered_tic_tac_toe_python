from dataclasses import dataclass, field
from typing import Any

from app.game_state.state_status import StateStatus

@dataclass
class StateTickResult():
  status: StateStatus
  next_state: str = ''
  inputs: dict[str, Any] = field(default_factory=dict)
