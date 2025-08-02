from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Roblox API is running!"

@app.route("/userinfo")
def get_user_info():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Step 1: Get userId from username
    url = "https://users.roblox.com/v1/usernames/users"
    response = requests.post(url, json={"usernames": [username]})
    data = response.json()

    if not data["data"]:
        return jsonify({"error": "User not found"}), 404

    user = data["data"][0]
    user_id = user["id"]

    # Step 2: Get profile and avatar
    profile = requests.get(f"https://users.roblox.com/v1/users/{user_id}").json()
    avatar = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=150x150&format=Png&isCircular=true").json()

    return jsonify({
        "username": profile["name"],
        "displayName": profile["displayName"],
        "userId": user_id,
        "description": profile["description"],
        "avatar": avatar["data"][0]["imageUrl"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
