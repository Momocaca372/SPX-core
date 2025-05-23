from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated example service
class ExampleService:
    def create(self, data):
        return {**data, "created": True}
    def update(self, data):
        return {**data, "updated": True}
    def delete(self, user_id):
        return {"deleted_id": user_id}
    def findById(self, user_id):
        return {"id": user_id, "user": "testuser"}
    def viewFriendsById(self, user_id):
        return {"id": user_id, "friends": ["u123", "u456"]}

exampleService = ExampleService()

@app.route("/api/user/create", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or not data.get("user") or not data.get("password"):
        return jsonify({"status": "failure", "error": "User and password are required"}), 400
    result = exampleService.create(data)
    return jsonify({"status": "success", "data": result})

@app.route("/api/user/update", methods=["POST"])
def update_user():
    data = request.get_json()
    if not data or not data.get("id"):
        return jsonify({"status": "failure", "error": "ID is required"}), 400
    result = exampleService.update(data)
    return jsonify({"status": "success", "data": result})

@app.route("/api/user/delete", methods=["POST"])
def delete_user():
    data = request.get_json()
    if not data or not data.get("id"):
        return jsonify({"status": "failure", "error": "ID is required"}), 400
    result = exampleService.delete(data["id"])
    return jsonify({"status": "success", "data": result})

@app.route("/api/user/find", methods=["GET"])
def find_by_id():
    user_id = request.args.get("id")
    if not user_id:
        return jsonify({"status": "failure", "error": "ID is required"}), 400
    result = exampleService.findById(user_id)
    return jsonify({"status": "success", "data": result})

@app.route("/api/user/friends", methods=["GET"])
def view_friends():
    user_id = request.args.get("id")
    if not user_id:
        return jsonify({"status": "failure", "error": "ID is required"}), 400
    result = exampleService.viewFriendsById(user_id)
    return jsonify({"status": "success", "data": result})

if __name__ == "__main__":
    app.run(debug=True)
