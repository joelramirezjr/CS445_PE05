from flask import Flask
from flask import request
import json

database = {}
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the To-Do List API!"

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))
        database[dict_json["name"]] = dict_json["status"]
        return 'Success', 200
    except Exception as e:
        print("Error during saving object:", e)
        return 'Failed', 400

# Retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    try:
        result = ""
        for name, status in database.items():
            result += f"{name}: {status}\n"
        if result == "":
            return 'No tasks found', 200
        return result.strip(), 200
    except Exception as e:
        print("Error while fetching records:", e)
        return 'Error', 400

# Update a task
@app.route('/tasks', methods=['PUT'])
def update_task():
    try:
        data = request.json
        dict_json = json.loads(json.dumps(data))
        if dict_json["name"] in database:
            database[dict_json["name"]] = dict_json["status"]
            return 'Success', 200
        else:
            return 'Task Not Found', 404
    except Exception as e:
        print("Error during updating object:", e)
        return 'Failed', 400

# Delete a task
@app.route('/tasks/<task_name>', methods=['DELETE'])
def delete_task(task_name):
    try:
        if task_name in database:
            database.pop(task_name)
            return 'Record deleted successfully', 200
        else:
            return 'Task Not Found', 404
    except Exception as e:
        print("Error while removing record:", e)
        return 'Error while removing record', 400

if __name__ == "__main__":
    app.run(debug=True)