import datetime


def get_date_from():
    date_from = datetime.date.today()- datetime.timedelta(days=+7)
    return date_from.isoformat()


def get_date_to():
    date_to = datetime.date.today().isoformat()
    return date_to