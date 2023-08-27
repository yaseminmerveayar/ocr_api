import re

async def parse_id_number(text: str):
    pattern = r"\b\d{11}\b"
    matches: list = re.findall(pattern, text)

    ids = set()

    if matches:
        for id in matches:
            if await id_check(id):
                ids.add(id)

    ids_list = list(ids)  # Set'i liste olarak çeviriyoruz

    urls_data = [{"value": id, "type": "ID_NUMBER"} for id in ids_list]
    return urls_data



async def id_check(tc_id: str) -> bool:
    """
    Checks that if the given number is a valid TC ID number or not.
    """
    if int(tc_id[0]) < 1 or len(tc_id) != 11:
        return False

    eleventh_digit = sum(map(int, tc_id[0:10])) % 10
    if eleventh_digit != int(tc_id[10]):
        return False

    tenth_digit = (sum(map(int, tc_id[:10:2])) * 7-(
                sum(map(int, tc_id[1:9:2])))) % 10

    return tenth_digit == int(tc_id[9])