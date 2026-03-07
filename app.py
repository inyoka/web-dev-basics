# app.py — the main entry point for the Flask web application

# Import Flask and the helper functions we need
from flask import Flask, render_template, request

# Create the Flask app object — Flask uses __name__ to find the project folder
app = Flask(__name__)


# --- Routes ---
# A route tells Flask what to do when someone visits a particular URL.


# The home page — handles GET requests (simply loading the page)
@app.route("/")
def index():
    # Render (build and return) the index.html template
    return render_template("index.html")


# The result page — handles POST requests (form submissions)
@app.route("/result", methods=["POST"])
def result():
    # Read the values the user typed into the form
    student_name = request.form.get("student_name", "").strip()
    subject = request.form.get("subject", "")
    hours_raw = request.form.get("hours", "")

    # Allowed subject choices (must match the options in the HTML form)
    allowed_subjects = [
        "Maths", "Physics", "Computer Science",
        "Biology", "Chemistry", "History", "English",
    ]

    # Basic server-side validation — the HTML 'required' attribute helps too,
    # but server-side checks are always a good habit even for simple projects
    if not student_name or subject not in allowed_subjects:
        return render_template("index.html", error="Please fill in all fields correctly.")

    # Convert hours to a decimal number so we can compare it
    try:
        hours = float(hours_raw)
        if hours < 0 or hours > 12:
            raise ValueError
    except (ValueError, TypeError):
        hours = 0

    # Pass the values to the template so Jinja can display them
    return render_template(
        "result.html",
        student_name=student_name,
        subject=subject,
        hours=hours,
    )


# Run the development server when this file is executed directly
# debug=True gives helpful error messages — never use this in production!
if __name__ == "__main__":
    app.run(debug=True)
