import re


async def parse_plate(text: str):
    """
    Parse the text with pattern and extract plate

    Args:
        text : given text
    
    Return:
        List included all plates and type
    """

    pattern = r"\b\d{2}\s?[A-Z]{1,3}\s?\d{2,4}\b"
    matches: list = re.findall(pattern, text)
    plates = set()
    if matches:
        plates.update(matches)  # Benzersiz değerleri set'e ekliyoruz

    return [{"value": plate, "type": "PLATE"} for plate in plates]
