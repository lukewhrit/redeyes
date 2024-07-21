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

from flask import Flask

from redeyes import database, views, globals, api


def create_app(config) -> Flask:
    app = Flask("redeyes")

    # do migrations
    conn = database.connect(globals.DSN)
    database.migrate(conn)

    app.config.from_mapping({
        "JSON_SORT_KEYS": False,
        **config
    })

    app.register_blueprint(views.views)
    app.register_blueprint(api.api)

    return app
