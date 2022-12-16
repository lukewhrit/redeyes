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

import logging

from redeyes import db, globals, app

application = app.create_app({
    "DEBUG": False,
})

if __name__ == "__main__":
    # do migrations
    db.migrate(db.connect(globals.DSN))

    if globals.DEBUG:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    application.run(host=globals.HOST, port=globals.PORT, debug=globals.DEBUG)
