from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/scrape/<string:url>', methods=['GET'])
def get_web_content(url):
    return jsonify({"fetched_url": url})


@app.route('/test', methods=['GET'])
def get_test_functionality():
    return jsonify({"test": "test"})


if __name__ == '__main__':
    app.run(debug=True)