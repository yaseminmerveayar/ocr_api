import re

async def parse_phone_number(text):
    patterns = [
        r'(?:(?:\+?90\s?)|0\s?)?(?:(5[0-9]{2})(?:\s|-)?(\d{3})(?:\s|-)?(\d{2})(?:\s|-)?(\d{2}))',  # Cep telefonu numarası
    ]
    numbers = set()
    for pattern in patterns:
        matches = re.findall(pattern, text)

        if matches:
            for match in matches:
                formatted_number = ''.join(match).replace(" ", "")

                numbers.add(formatted_number)  # Benzersiz değerleri set'e ekliyoruz

    return [{"value": number, "type": "PHONE_NUMBER"} for number in numbers]
