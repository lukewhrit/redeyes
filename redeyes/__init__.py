"""
redeyes is an extremely simple URL shortener written in Python.

It is built with Flask and supports a wide range of different shortening styles
and configuration methods. The primary and currently only database adapter is
built using psycopg, for PostgreSQL, but redeyes is built in a way which it can
be extended with many other adapters in the future.
"""

"""
Copyright (C) 2022 Luke Whritenour

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

__version__ = "0.1.0"
