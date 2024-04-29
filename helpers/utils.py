import os
import shutil
import random
import string

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