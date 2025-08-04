 Court Case Info Fetcher

A Flask-based web application that allows users to enter court case details (case type, number, and year) and fetch information like parties, filing date, hearing date, and orders.

This project was built as part of an internship task, demonstrating skills in Flask, HTML, database logging, and deployment.

---
 Live Demo

🔗 https://court-case-fetcher.onrender.com

> ⚠️ Note: App may take 30–60 seconds to load on first visit due to Render’s free-tier sleep mode.

---

 Features

- Input court case details (type, number, year)
- Simulated or real-time data fetching logic
- Result display on same page
- All queries and results saved in SQLite database
- Clean HTML interface using Jinja templates

---

 Technologies Used

- Python (Flask)
- SQLite
- HTML / Jinja2 (for templating)
- Render.com (for deployment)

---
 Project Structure

```
court_data_fetcher/
├── app.py
├── court_scraper.py
├── database.py
├── templates/
│   └── index.html
├── case_queries.db
├── requirements.txt
└── README.md
```

---

 How to Run Locally

1. Clone this repo  
   ```bash
   git clone https://github.com/VengGaurav/court-case-fetcher.git
   cd court-case-fetcher
   ```

2. Create a virtual environment (optional but recommended)  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app  
   ```bash
   python app.py
   ```

5. Open in browser:  
   http://localhost:5000

---
 Deployment (Render)

This app is deployed on [Render.com](https://render.com/) using:
- Python 3.11+
- Build command: `pip install -r requirements.txt`
- Start command: `python app.py`

---

 Author

**Gaurav Vengurlekar**  
🔗 https://github.com/VengGaurav

---

 License

This project is for internship/demo purposes. Feel free to fork and improve.
