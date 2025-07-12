
def validate_national_code(code):
    return len(code) == 10 and code.isdigit()

def validate_phone_number(phone):
    return phone.startswith("09") and len(phone) == 11

def validate_passport_number(passport):
    return len(passport) >= 8
