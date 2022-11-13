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

import psycopg2
import logging

def write_entry(conn):
    cur = conn.cursor()

    cur.execute("SELECT * FROM ")
    return

def read_entry(conn):
    return

def connect(dsn):
    try:
        conn = psycopg2.connect(dsn)
        logging.info("Successfully connected to PostgreSQL database")
        return conn
    except:
        logging.critical("Database did not connect successfully")
        exit(1)
