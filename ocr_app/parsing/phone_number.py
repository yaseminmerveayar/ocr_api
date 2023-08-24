import re
text = """tel no 05378105050
    5368456758 invalid olarak 530 984 45 47  
    530 456 3748  +905378293556 0 555 123 45 67"""
async def parse_phone_number(text):
    patterns = [
        r'(?:(?:\+?90\s?)|0\s?)?(?:(\d{3})[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})|(\d{4})(\d{3})(\d{2})(\d{2}))',  # Cep telefonu numarası
        r"^(0)([2348]{1})([0-9]{2})\s?([0-9]{3})\s?([0-9]{2})\s?([0-9]{2})$",
    ]
    numbers = set()
    for pattern in patterns:
        matches = re.findall(pattern, text)

        if matches:
            for match in matches:
                formatted_number = ''.join(match).replace(" ", "")
                print(formatted_number)
                numbers.add(formatted_number)  # Benzersiz değerleri set'e ekliyoruz

    return [{"value": number, "type": "PHONE_NUMBER"} for number in numbers]
