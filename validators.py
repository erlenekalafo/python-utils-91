import re

class Validator:
    @staticmethod
    def validate_email(email: str) -> bool:
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(regex, email) is not None
    
    @staticmethod
    def validate_phone(phone: str) -> bool:
        regex = r'^\+?1?\d{9,15}$'
        return re.match(regex, phone) is not None
    
    @staticmethod
    def validate_url(url: str) -> bool:
        regex = r'^(http:\/\/|https:\/\/)?(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+$'
        return re.match(regex, url) is not None
    
    @staticmethod
    def validate_password(password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search('[A-Z]', password):
            return False
        if not re.search('[0-9]', password):
            return False
        return True

