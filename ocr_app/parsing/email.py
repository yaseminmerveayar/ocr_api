import re
import validators


async def parse_email(text: str):
    pattern = r"\b[\w.-]+?@\w+?\.\w+?\b"
    matches: list = re.findall(pattern, text)
    emails = []
    if matches:
        for email in matches:
            if validators.email(email):
                emails.append({"value": email, "type": "email", "is_valid": True})
            else:
                emails.append({"value": email, "type": "email", "is_valid": False})

    return emails
