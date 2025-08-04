import os
from flask import Flask, render_template, request
from court_scraper import fetch_case_data
from database import init_db, log_query

app = Flask(__name__)

# Ensure database is initialized
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        case_type = request.form["case_type"]
        case_number = request.form["case_number"]
        filing_year = request.form["filing_year"]

        result = fetch_case_data(case_type, case_number, filing_year)
        log_query(case_type, case_number, filing_year, result)

    return render_template("index.html", result=result)

# Render-compatible app launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's dynamic port
    app.run(host="0.0.0.0", port=port)
