from flask import Flask, request, jsonify

from services.items_service import ItemsService

app = Flask(__name__)
items_service = ItemsService()
@app.route('/')
def home():
    return {"hello": "world"}


# Define a POST route
@app.route('/submit', methods=['POST'])
def submit():
    # Access form data sent in the POST request
    data = request.get_json()  # for JSON data
    name = data.get('name')
    age = data.get('age')

    # You can also use request.form for form-encoded data (from HTML forms)
    # name = request.form.get('name')
    # age = request.form.get('age')

    # Respond back with the received data
    return jsonify({
        "message": "Data received successfully",
        "name": name,
        "age": age
    })

# Define a GET route
@app.route('/data', methods=['GET'])
def get_all_data():
    return jsonify(items_service.get_all_items())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
