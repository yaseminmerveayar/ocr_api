import re


async def parse_phone_number(text):
    """
    Parse the text with pattern and extract phone number

    Args:
        text : given text
    
    Return:
        List included all phone numbers and type
    """
    patterns = [
        r"\b(?:\+?90)?[5-9][0-9]{9}\b",  # Cep telefonu numarası
    ]
    numbers = set()
    for pattern in patterns:
        matches = re.findall(pattern, text)

        if matches:
            for match in matches:
                formatted_number = "".join(match).replace(" ", "")

                numbers.add(formatted_number)  # Benzersiz değerleri set'e ekliyoruz

    return [{"value": number, "type": "PHONE_NUMBER"} for number in numbers]
