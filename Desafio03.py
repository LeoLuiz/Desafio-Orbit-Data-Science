from flask import Flask, jsonify
import csv
import os

app = Flask(__name__)

def read_comments_from_csv():
    csv_filename = "comments.csv"
    if os.path.exists(csv_filename):
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            comments = [row for row in csv_reader]
        return comments
    else:
        return []

@app.route('/api/comments', methods=['GET'])
def get_comments():
    comments = read_comments_from_csv()
    return jsonify(comments)

if __name__ == '__main__':
    app.run(debug=True)