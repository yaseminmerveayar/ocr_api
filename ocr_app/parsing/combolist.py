import re


# ^([^:\s]+:[^\s]+)$
# r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+:[a-zA-Z0-9._-]+'
async def parse_combolist(text: str):
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9.-]+:[a-zA-Z0-9._-]+"
    matches: list = re.findall(pattern, text)
    combolists = set()
    if matches:
        combolists.update(matches)  # Benzersiz değerleri set'e ekliyoruz

    return [{"value": combolist, "type": "COMBOLIST"} for combolist in combolists]
