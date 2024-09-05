"""
Copyright (C) 2022-2024 Luke Whritenour

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from os import environ as env

from redeyes.__init__ import __version__

VERSION = __version__
DEBUG = env.get("DEBUG", True)
SLUG_LENGTH = env.get("REDEYES_SLUG_LENGTH", "6")
DSN = env.get("REDEYES_DSN", "sqlite:///database.db")
PORT = env.get("REDEYES_PORT", "80")
HOST = env.get("REDEYES_HOST", "0.0.0.0")
