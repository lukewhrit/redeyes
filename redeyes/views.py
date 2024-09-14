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
            link = database.Link(id=id, long=body["link"])

            database.db.session.add(link)
            database.db.session.commit()

            return render_template("index.html", version=globals.VERSION,
                                   link="%s/%s" % (request.host, id))
        else:
            return "Not a URL", 400

        return render_template("index.html", version=globals.VERSION, link=id)

    return render_template("index.html", version=globals.VERSION)


@views.get("/<id>")
def fetch(id):
    link = database.db.get_or_404(database.Link, id)

    link.visits += 1
    link.last_visited = database.db.func.now()

    database.db.session.commit()

    return redirect(link.long, code=308)


@views.get("/links")
def dashboard():
    links = database.db.session.query(database.Link).all()
    short = request.args.get("short")

    if short:
        m = [o for o in links if o.id == short]

        return render_template(
            "links.html", version=globals.VERSION,
            link=m[0], links=links,
        )

    return render_template(
        "links.html", version=globals.VERSION,
        link={}, links=links,
    )
