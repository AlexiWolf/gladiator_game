#  Copyright (C) 2021 AlexiWolf
#
#  Gladiator is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Gladiator is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Gladiator.  If not, see <https://www.gnu.org/licenses/>.
#


"""Console script for gladiator_game."""


import argparse
import sys


def main():
    """Console script for gladiator_game."""
    parser = argparse.ArgumentParser()
    parser.add_argument("_", nargs="*")
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into " "gladiator_game.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
