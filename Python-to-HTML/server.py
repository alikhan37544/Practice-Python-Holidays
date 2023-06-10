from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json() # Get data from the request
    # Process the data as needed (e.g., save to database, perform calculations, etc.)

    # Prepare the response message
    message = "Data submitted successfully!"

    return jsonify({"message": message})

if __name__ == "__main__":
    app.run()
