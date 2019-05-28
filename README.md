# Rock-Paper-Scissors (Python)

A basic game written in Python.

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Fork the repository from [GitHub source](https://github.com/prof-rossetti/rock-paper-scissors-py).

Then use GitHub Desktop or the command-line to "clone" or download your fork onto your local computer:

```sh
git clone https://github.com/YOUR_USERNAME/rock-paper-scissors-py.git # this is the HTTP address, but you could alternatively use the SSH address
```

Navigate into your local repo from the command-line before running any of the other commands below:

```sh
cd rock-paper-scissors-py
```

## Setup

Create and activate a new Anaconda virtual environment:

```sh
conda create -n game-env python=3.7 # first time only
conda activate game-env
```

## Usage

Play the game from the command-line:

```sh
python app/game.py
```

Play the game from a `tkinter` GUI:

```sh
python app/tk_game.py
```

## Testing

Install pytest (first time only):

```sh
pip install pytest
```

Run tests:

```sh
pytest
```

## [License](/LICENSE.md)
