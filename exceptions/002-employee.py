from datetime import datetime

AVAILABLE_DEPARTMENTS = [
    "it", "sale", "accountant"
]
FOUNDATION_YEAR = 2010


class Employee:
    def __init__(
        self, first_name: str, last_name: str, department: str, year_of_employment: int
    ):
        self.first_name = first_name
        self.last_name = last_name

        if department not in AVAILABLE_DEPARTMENTS:
            raise ValueError("No department found")

        self.department = department

        today_year = datetime.today().year
        if not FOUNDATION_YEAR <= year_of_employment <= today_year:
            raise ValueError(f"Invalid year. Should be between {FOUNDATION_YEAR} and {today_year} included.")

        self.year_of_employment = year_of_employment


