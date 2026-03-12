from flask import Flask, render_template, request

app = Flask(__name__)

def meters_to_feet(m):
    return m * 3.28084

def feet_to_meters(ft):
    return ft / 3.28084

def inches_to_centimeters(inches):
    return inches * 2.54

def centimeters_to_inches(cm):
    return cm / 2.54

def kilometers_to_meters(km):
    return km * 1000

def meters_to_kilometers(m):
    return m / 1000 

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            value = float(request.form["value"])
            unit_from = request.form["unit_from"]
            unit_to = request.form["unit_to"]

            if unit_from == "m" and unit_to == "ft":
                result = meters_to_feet(value)
            elif unit_from == "ft" and unit_to == "m":
                result = feet_to_meters(value)
            elif unit_from == "in" and unit_to == "cm":
                result = inches_to_centimeters(value)
            elif unit_from == "cm" and unit_to == "in":
                result = centimeters_to_inches(value)
            elif unit_from == "km" and unit_to == "m":
                result = kilometers_to_meters(value)
            elif unit_from == "m" and unit_to == "km":
                result = meters_to_kilometers(value)
            elif unit_from == "kg" and unit_to == "lb":
                result = kg_to_pounds(value)
            elif unit_from == "lb" and unit_to == "kg":
                result = pounds_to_kg(value)
            else:
                error = "That conversion is not supported yet."
        except ValueError:
            error = "Please enter a valid number."

    return render_template("index.html",
                           result=result,
                           error=error)

if __name__ == "__main__":
 app.run(debug=True, host="0.0.0.0",
port=8080)  