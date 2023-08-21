import re

async def parse_combolist(text: str):
    pattern = r"\S+:\S+"
    matches: list = re.findall(pattern, text)
    combolists = []
    if matches:
        for combolist in matches:
            combolists.append({"value": combolist, "type": "combolist"})

    return combolists
