# UneVieDeFourmi

Algorithm class project.

## Goal of the project
Make all the ants go from the anthill entrance (`Sv`) to the exit (`Sd`) in as few steps as possible.
The anthill is a graph: rooms are nodes, tunnels are edges, and each room can hold a limited number of ants.

## Requirements
* Python 3 (files were first run with Python 3.10)
* pandas, numpy, networkx, matplotlib
* numpy older than 2.4 (for example `pip install "numpy<2"`): with newer versions `import_data` in `functions.py` stops with a `TypeError`

```
pip install pandas "numpy<2" networkx matplotlib
```

## Instructions
1. Put the anthill description files in a folder named `Fourmilieres`, **next to** the project folder (not inside it): `../Fourmilieres/fourmiliere_un.txt`, `fourmiliere_deux.txt`, `fourmiliere_trois.txt`, `fourmiliere_quatre.txt`, `fourmiliere_cinq.txt`.
   These files are not in the repository (`*.txt` is ignored by git).
2. Run `python main.py` from the project folder.
3. Type the anthill number (1 to 5) when asked.

## Data file format
* First line: number of ants, written `f=<number>` (example: `f=3`).
* Then one line per room, except `Sv` and `Sd` which are added automatically: `name`, or `name x capacity`.
  Without a capacity, a room holds 1 ant. The middle value is not used by the program.
* Then one line per tunnel: `room1 - room2` (with spaces around the dash). Tunnels can go both ways.

Example:

```
f=3
S1
S2 1 2
Sv - S1
S1 - S2
S2 - Sd
S1 - Sd
```

## How it works
At each step, every ant that is not yet in `Sd` tries to move once:
1. Dead ends already found are ignored.
2. If the ant has only one way out and it is the room it came from, the room is marked as a dead end and the ant goes back.
3. If `Sd` is next to the ant, it goes to `Sd`.
4. Otherwise it goes to the neighbour with the lowest estimated distance to the exit (`to_end`), chosen randomly in case of a tie. It does not go back to the room it came from if another choice exists, and a room that is full is skipped.
5. After a move, the estimated distance of the room the ant left is updated.

The loop stops when all ants are in `Sd`. As there is some randomness, the number of steps can change from one run to another.

## Output
* Console: the moves of each step (`ant 0 : from Sv to S1`).
* `output.txt`: the same moves. The file is **appended** at each run, delete it to start a new log.
* An animation window showing the anthill step by step (1 second per step), and one image per step saved in the project folder (`0.png`, `1.png`, ...).

Colours in the animation:
* orange: entrance `Sv`
* blue: empty room
* grey: room with ants
* red: dead end
* green: exit `Sd` when all ants have arrived

Each room shows its name, its number of ants and the estimated distance to the exit (`-->3`). The size of a room depends on its capacity.

## Files
* `main.py`: asks the anthill number, runs the simulation and shows the animation.
* `classes.py`: `Ant` (index, current room, previous room, steps) and `Anthill` (ants, graph built with networkx, data for the animation).
* `functions.py`: `import_data`, reads the data file and returns ants, rooms and tunnels.

## Known limits
* The data files must be provided separately (see Instructions).
* The result is not guaranteed to be the shortest solution: ants choose their way one step at a time.
