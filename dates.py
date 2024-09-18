from datetime import datetime

def convert_to_date(date_str):
    try:
        date_object = datetime.strptime(date_str, "%Y-%m-%d").date()
        return date_object
    except ValueError:
        raise ValueError(f"The date {date_str} does not ahve the format YYYY-MM-DD")

def get_today():
    return datetime.today().date()
