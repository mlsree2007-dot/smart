from flask_cors import CORS
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)
CORS(app)


# Simulated book database
book_db = {
    "BOOK001": {"location": "Shelf A1", "timestamp": "2025-11-03T18:45:00"},
    "BOOK002": {"location": "Shelf B2", "timestamp": "2025-11-03T18:47:30"},
    "BOOK003": {"location": "Shelf C3", "timestamp": "2025-11-03T18:50:15"},
}

@app.route('/search')
def search_book():
    tag_id = request.args.get("tag_id")
    if tag_id in book_db:
        return jsonify({
            "found": True,
            "tag_id": tag_id,
            "location": book_db[tag_id]["location"],
            "timestamp": book_db[tag_id]["timestamp"]
        })
    else:
        return jsonify({"found": False})

if __name__ == '__main__':
    app.run()

