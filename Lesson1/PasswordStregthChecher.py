password = input("Enter your password: ")
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
is_long_enough = len(password) >= 8
missing = []
if not is_long_enough:
    missing.append("at least 8 characters long")
if not has_upper:
    missing.append("an uppercase letter")
if not has_lower:
    missing.append("a lowercase letter")
if not has_digit:
    missing.append("a digit")
if not missing:
    print("Strong password")
else:
    print("Weak password. Your password is missing:", ", ".join(missing))