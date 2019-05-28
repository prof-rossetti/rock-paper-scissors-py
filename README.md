# Rock-Paper-Scissors (Python)

[![Build Status](https://travis-ci.com/prof-rossetti/rock-paper-scissors-py.svg?branch=master)](https://travis-ci.com/prof-rossetti/rock-paper-scissors-py)

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

The only game which requires package installation is the `PySimpleGUI` Game, so if you want to play that one, you'll need to install the package first:

```sh
pip install PySimpleGUI pillow
```

## Usage

### CLI Game

Play the game from the command-line:

```sh
python app/game.py
```

![a screenshot of gameplay](/img/game_screenshot.png)

### `tkinter` GUI Game

Play the game from a `tkinter` GUI:

```sh
python app/tk_game.py
```

![a screenshot of gameplay](/img/tk_game_screenshot_with_img.png)

### `PySimpleGUI` Game

Play the game from a `PySimpleGUI` GUI:

```sh
python app/sg_game.py
```

![a screenshot of gameplay](/img/sg_game_screenshot.png)


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
