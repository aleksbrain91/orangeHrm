import os
import shutil
import random
import string
from datetime import datetime, timedelta


class Utils:

    @staticmethod
    def generate_random_email(domain='example.com', length=15):
        characters = string.ascii_letters + string.digits
        local_part = ''.join(random.choice(characters) for i in range(length))
        return f"{local_part}@{domain}"

    @staticmethod
    def generate_random_string(length=15):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for i in range(length))
        return random_string

    @staticmethod
    def generate_random_date():
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2024, 5, 13)
        days_diff = (end_date - start_date).days
        random_days = random.randint(0, days_diff)
        random_date = start_date + timedelta(days=random_days)
        return random_date.strftime("%Y-%m-%d")