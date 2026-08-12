def validate_email(email):

    email = email.strip()

    if email.count("@") != 1:
        return "Invalid: Email must contain exactly one @"
    username, domain = email.split("@")
    if username == "":
        return "Invalid: Username is empty"
    if domain == "":
        return "Invalid: Domain is empty"
    if "." not in domain:
        return "Invalid: Domain must contain ."
    if domain.startswith(".") or domain.endswith("."):
        return "Invalid: Incorrect dot position"
    if " " in email:
        return "Invalid: Email cannot contain spaces"
    allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-@"
    for char in email:
        if char not in allowed:
            return "Invalid: Contains invalid character"

    return "Valid Email"
email = input("Enter your email: ")
result = validate_email(email)
print(result)