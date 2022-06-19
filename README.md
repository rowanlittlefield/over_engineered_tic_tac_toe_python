# Over Engineered Tic Tac Toe: Python

A CLI application written in Python for playing tic-tac-toe.

## Screenshot

### Main Menu

<img width="170" alt="Screen Shot 2022-06-10 at 11 47 10 AM" src="https://user-images.githubusercontent.com/30376211/174488257-8a8f9e60-1d40-4be7-bedc-7bcd8c951e24.png">

### Match

<img width="68" alt="Screen Shot 2022-06-10 at 11 47 40 AM" src="https://user-images.githubusercontent.com/30376211/174488316-319455d5-64b0-4957-bb8d-dbefcfb5d5b3.png">

## How to Run

1. [Clone](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository#_git_cloning) this repo.

2. [Install Python](https://realpython.com/installing-python/).

3. Navigate to the cloned project directory in your command line. The game can be run from this directory using `python main.py`. To run the unit tests for this project, run `python3 -m pytest`. Instructions for installing `pytest` can be found [here](https://docs.pytest.org/en/7.1.x/getting-started.html).

## Functionality and MVP

### Controls

The control scheme is described below. Type any of the following characters followed by the enter/return key to send input to the application.

* `w` - Move cursor up by one space.
* `d` - Move cursor right by one space.
* `s` - Move cursor down by one space.
* `a` - Move cursor left by one space.
* `f` - Performs a return/enter. When on the main menu, this will perform the action selected in the menu. When in a match, this will set the space currently occupied by the board cursor with the marker (X or O) associated with the current player. If the selected space is already occupied, then nothing will happen.
* `u` - Undo the previous turn. This will decrement the displayed turn number, remove the marker set in the previous turn, move the cursor to the previously set space, and toggle the current user. This command does nothing on turn 1. This command only works when playing a match. The command does nothing on the main menu.
* `r` - Redo an undone turn. Reverses all changes from the last undo command. *Note:* The redo cache will be cleared if you undo a command, then set a new space prior to redo. This command only works when playing a match. The command does nothing on the main menu.
* `g` - Saves the progress of the current match. The match can be revisited later by selecting the `Load Game` option when in the main menu. Note, this input can only be used to save a game when in a match. The command does nothing on the main menu.

### State-machine Based Navigation

In this project, the `Game` class encapsulates the primary application logic. The `Game` class implements the [state pattern](https://en.wikipedia.org/wiki/State_pattern) and behaves similarly to a [finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine). Within the context of this pattern, the possible *concrete states* include the `MainMenu` and `Match` classes (both instances of the abstract class `GameState`), while the role of *context* is handled by the `Game` class.

Calling the `play` method on an instance of `Game` will initiate the gameplay loop. A single iteration of this loop is referred to as a tick. During a single tick, the `Game` instance will do the following in order:

1. Render in the terminal. This is done by clearing the terminal and then calling render on the game's current `GameState` instance (which is stored on the `state` attribute).
2. Retrieve input from the user, which is mapped to an instance of the `UserAction` enum.
3. Pass the `UserAction` to the current state via `GameStates`'s `play_tick` method. This method returns an instance of `StateTickResult`.
4. Check the status of the `StateTickResult` produced in the previous step. If the status is `StateStatus.COMPLETED`, then the game undergoes a state change whose inputs and next state are specified by the `StateTickResult`.

### History Feature

The history feature (undo and redo commands) utilize the well-known [memento pattern](https://en.wikipedia.org/wiki/Memento_pattern), where the `Board` class (`app/game_state/match/board.py`) acts as the *originator*, the `BoardMemento` class (`app/game_state/match/board_memento.py`) acts as the *memento*, and the `MatchHistory` class (`app/game_state/match/match_history.py`) acts as the *caretaker*.

Remaining TODOS

* Add Readme
* Final QA/Bugfixes
* Upload to Github
