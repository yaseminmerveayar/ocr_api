import re


async def parse_credit_card(text: str):
    """
    Parse the text with pattern and extract credit card number

    Args:
        text : given text
    
    Return:
        List included all valid credit card numbers and type
    """
    pattern = r"(?:\d{4}-){3}\d{4}|\d{16}"
    matches: list = re.findall(pattern, text)

    cards = set()

    if matches:
        for card_number in matches:
            card_number = card_number.replace("-", "")
            card_number = card_number.replace(" ", "")

            if await luhn_check(card_number):
                cards.add(card_number)

    cards_list = list(cards)  # Set'i liste olarak çeviriyoruz

    cards_data = [{"value": card, "type": "CREDIT_CARD_NUMBER"} for card in cards_list]
    return cards_data


async def luhn_check(card_number):
    """
    Checks that if the given number is a valid card number or not.

    Args:
        card_number : given card number
    
    Return:
        Boolean value - if valid return True
    """

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
