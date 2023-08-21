import re


async def parse_credit_card(text: str):
    pattern = r"(?:\d{4}-){3}\d{4}|\d{16}"
    matches: list = re.findall(pattern, text)

    cards = []

    if matches:
        for card_number in matches:
            card_number = card_number.replace("-", "")
            card_number = card_number.replace(" ", "")

            if await luhn_check(card_number):
                cards.append(
                    {"value": card_number, "type": "credit_card", "is_valid": True}
                )
            else:
                cards.append(
                    {"value": card_number, "type": "credit_card", "is_valid": False}
                )

    return cards


async def luhn_check(card_number):
    reversed_number = card_number[::-1]

    doubled_digits = []
    for i in range(len(reversed_number)):
        digit = int(reversed_number[i])
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        doubled_digits.append(digit)

    total_sum = sum(doubled_digits)

    return total_sum % 10 == 0
