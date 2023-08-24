import re
import validators


async def parse_email(text: str):
    pattern = r"\b[\w.-]+?@\w+?\.\w+?\b"
    matches: list = re.findall(pattern, text)

    emails = set()

    if matches:
        for email in matches:
            if validators.email(email):
                emails.add(email)  # Benzersiz URL'leri set'e ekliyoruz

    email_list = list(emails)  # Set'i liste olarak çeviriyoruz

    urls_data = [{"value": email, "type": "EMAIL"} for email in email_list]
    return urls_data
