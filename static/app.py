from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='static')

# Temporary storage for user data
users = []

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/register')
def register():
    return send_from_directory('static', 'register.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    # Handle user login logic here
    return jsonify({"message": "Login successful", "data": data})

@app.route('/api/register', methods=['POST'])
def register_user():
    data = request.json
    users.append(data)  # Store user data in the list
    return jsonify({"message": "Registration successful", "data": data})

# New endpoint to retrieve user data
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)  # Return the list of users as JSON

if __name__ == '__main__':
    app.run(debug=True)
