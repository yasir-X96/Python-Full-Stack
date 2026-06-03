def validate_mobile_number(number: str) -> bool:
    return number.isdigit() and len(number) == 10

def validate_age(age: int) -> bool:
    return 0 < age < 120

def validate_policy_duration(duration: int) -> bool:
    return duration > 0
