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

from __init__ import __version__
from flask import Flask, request, render_template, redirect
from urllib.parse import urlparse
import logging
import random
import redeyes.db

DEBUG = True
SLUG_LENGTH = 6
DSN = "host=localhost port=5432 dbname=whrit user=whrit"

app = Flask("redeyes")
app.config.from_mapping({
    "JSON_SORT_KEYS": False,
    "DEBUG": DEBUG
})

def generate_id():
    random_string = ""

    for _ in range(SLUG_LENGTH):
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)

        random_integer = random_integer - 32 if flip_bit == 1 else random_integer

        random_string += (chr(random_integer))

    return random_string

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        id = generate_id()
        body = request.form.to_dict()
        link = urlparse(body["link"])

        if link.scheme and link.netloc:
            conn = redeyes.db.connect(DSN)
            cur = conn.cursor()

            cur.execute("INSERT INTO links (id, long) VALUES (%s, %s)",
                        (id, body["link"]))

            cur.close()
            conn.commit()

            print(request.host_url)

            return render_template("index.html", version=__version__, link="%s/%s" % (request.host, id))
        else:
            print("failed")


        return render_template("index.html", version=__version__, link=id)

    return render_template("index.html", version=__version__)

@app.get("/<id>")
def fetch(id):
    conn = redeyes.db.connect(DSN)
    cur = conn.cursor()

    cur.execute("SELECT long FROM links WHERE id='%s'" % (id))
    link = cur.fetchone()

    print(link)

    cur.close()
    conn.commit()

    return redirect(link[0], code=308)

if __name__ == "__main__":
    if DEBUG:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    redeyes.db.migrate(redeyes.db.connect(DSN))

    app.run()

