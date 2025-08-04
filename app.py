from flask import Flask, render_template, request
from court_scraper import fetch_case_data
from database import init_db, log_query

app = Flask(__name__)
init_db()  # initialize the database once

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        filing_year = request.form['filing_year']
        result = fetch_case_data(case_type, case_number, filing_year)

        # Save to database
        log_query(case_type, case_number, filing_year, result)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
