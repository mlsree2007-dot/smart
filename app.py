from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/simulate')
def simulate_scan():
    sample_tags = ['BOOK001', 'BOOK002', 'BOOK003']
    sample_locations = ['Shelf A1', 'Shelf B2', 'Shelf C3']
    return jsonify({
        "tag_id": random.choice(sample_tags),
        "location": random.choice(sample_locations),
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run()
