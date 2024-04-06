from flask import Flask, jsonify
from flask import request


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
   



app = Flask(__name__)



@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

@app.route('/todos', methods=['DELETE'])
def delete_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'










if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)