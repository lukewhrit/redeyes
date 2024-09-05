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

from flask import Flask

from redeyes import api, database, globals, views


def create_app(config) -> Flask:
    app = Flask("redeyes")

    # sqlalchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = globals.DSN
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    database.db.init_app(app)

    with app.app_context():
        database.db.create_all()

    app.config.from_mapping({
        "JSON_SORT_KEYS": False,
        **config
    })

    app.register_blueprint(views.views)
    app.register_blueprint(api.api)

    return app
