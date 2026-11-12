"""Tiny Realms: start the game with  python main.py

The game's code is in the game folder, its pictures and sounds in assets, the computer players in trained_ai."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "game"))

import app  # noqa: E402

if __name__ == "__main__":
    app.run()
