from flask import Flask, render_template, request, jsonify

app = Flask(
    __name__,
    template_folder="/Users/mustafagumustas/mustafagumustas.github.io/templates",
)


@app.route("/", methods=["GET"])
def home():
    return render_template("age_calculator.html")


@app.route("/calculate_age", methods=["POST"])
def calculate_age():
    try:
        age = int(request.form["age"])
        # Perform your age calculation here
        calculated_age = 2023 - age  # Replace this with your actual calculation
        return jsonify({"calculated_age": calculated_age})
    except ValueError:
        return jsonify({"error": "Invalid input"})


if __name__ == "__main__":
    app.run(debug=True)
