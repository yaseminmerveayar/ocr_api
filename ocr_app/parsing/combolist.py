import re


async def parse_combolist(text: str):
    """
    Parse the text with pattern and extract combolist

    Args:
        text : given text
    
    Return:
        List included all combolist and type
    """
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+:[a-zA-Z0-9._-]+"
    matches: list = re.findall(pattern, text)
    combolists = set()
    if matches:
        combolists.update(matches)  # Benzersiz değerleri set'e ekliyoruz

    return [{"value": combolist, "type": "COMBOLIST"} for combolist in combolists]
