import random
from urllib.parse import urlparse

from flask import Blueprint, redirect, render_template, request

from redeyes import database, globals

views = Blueprint('views', __name__)


def generate_id():
    random_string = ""

    for _ in range(6):
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)

        random_integer = random_integer - 32 if flip_bit == 1 else random_integer

        random_string += (chr(random_integer))

    return random_string


@views.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        id = generate_id()
        body = request.form.to_dict()
        link = urlparse(body["link"])

        if link.scheme and link.netloc:
            conn = database.connect(globals.DSN)
            cur = conn.cursor()

            cur.execute("INSERT INTO links (id, long) VALUES (%s, %s)",
                        (id, body["link"]))

            cur.close()
            conn.commit()

            return render_template("index.html", version=globals.VERSION,
                                   link="%s/%s" % (request.host, id))
        else:
            print("failed")

        return render_template("index.html", version=globals.VERSION, link=id)

    return render_template("index.html", version=globals.VERSION)


@views.get("/<id>")
def fetch(id):
    conn = database.connect(globals.DSN)
    cur = conn.cursor()

    cur.execute("SELECT long FROM links WHERE id='%s'" % (id))
    link = cur.fetchone()

    cur.close()
    conn.commit()

    return redirect(link[0], code=308)
