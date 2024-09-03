from urllib.parse import urlparse

from flask import Blueprint, jsonify, request

from redeyes import database, globals
from redeyes.views import generate_id

api = Blueprint('api', __name__)


@api.route("/api/v1/shorten", methods=["POST"])
def shorten():
    if not request.is_json and not request.form:
        return jsonify({"error": "Unsupported media type: must be application/json or "
                                 "multipart/form-data"}), 415

    body = request.form.to_dict() or request.get_json(silent=True)

    if not body.get("link"):
        return jsonify({"error": "Missing required parameter: link"}), 400

    id = generate_id()
    link = urlparse(body["link"])

    if link.scheme and link.netloc:
        conn = database.connect(globals.DSN)
        cur = conn.cursor()

        cur.execute("INSERT INTO links (id, long) VALUES (%s, %s)",
                    (id, body["link"]))

        cur.close()
        conn.commit()

        return jsonify({"short": id})

    return jsonify({"error": "Invalid URL"}), 400


@api.route("/api/v1/fetch", methods=["GET"])
def fetch():
    short = request.args.get("short")

    if not short:
        return jsonify({"error": "Missing required parameter: short"}), 400

    try:
        conn = database.connect(globals.DSN)
        cur = conn.cursor()

        cur.execute("SELECT long FROM links WHERE id='%s'" % (short))
        link = cur.fetchone()

        cur.close()
        conn.commit()

        return jsonify({"long": link[0]})
    except Exception:
        return jsonify({"error": "Link not found"}), 404
