import re

class InputValidator:
    def __init__(self):
        self.email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    def is_valid_email(self, email):
        return bool(self.email_regex.match(email))

    def is_valid_phone(self, phone):
        return len(phone) == 10 and phone.isdigit()

    def validate_user_details(self, user_details):
        if not isinstance(user_details, dict):
            raise ValueError('User details must be a dictionary')

        email = user_details.get('email')
        phone = user_details.get('phone')

        if not self.is_valid_email(email):
            raise ValueError('Invalid email format')
        if not self.is_valid_phone(phone):
            raise ValueError('Invalid phone number')

        return True  # Returns True if validation passes

# Example usage:
# validator = InputValidator()
# print(validator.validate_user_details({'email': 'test@example.com', 'phone': '1234567890'}))  
