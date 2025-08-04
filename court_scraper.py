import random
from datetime import datetime, timedelta

def fetch_case_data(case_type, case_number, filing_year):
    # Generate random party names
    parties_list = [
        "Rahul Sharma vs State of Haryana",
        "Sunita Devi vs Govt of UP",
        "Amit Kumar vs Reliance Ltd",
        "XYZ Pvt Ltd vs ABC Corporation",
        "Manoj Batra vs Income Tax Department",
        "Neha Joshi vs State Bank of India",
        "Rohan Mehta vs LIC of India",
        "Suresh Traders vs Flipkart Pvt Ltd"
    ]

    # Generate random future hearing date
    random_days = random.randint(10, 60)
    next_hearing_date = (datetime.now() + timedelta(days=random_days)).strftime("%Y-%m-%d")

    # Generate fake order URL
    order_url = f"https://example.com/orders/{case_type}{case_number}{filing_year}.pdf"

    # Build simulated response
    return {
        "Case Type": case_type,
        "Case Number": case_number,
        "Filing Year": filing_year,
        "Parties": random.choice(parties_list),
        "Filing Date": f"{filing_year}-01-01",
        "Next Hearing": next_hearing_date,
        "Latest Order": order_url
    }
