import re


async def parse_date(text: str):
    regex_list = {
        "dd/mm/yyyy - Date": r"[\d]{1,2}/[\d]{1,2}/[\d]{4}",
        "dd-mm-yyyy - Date": r"[\d]{1,2}-[\d]{1,2}-[\d]{2}",
        "dd Month yyyy - Date": r"[\d]{1,2} [ADFJMNOS]\w* [\d]{4}",
        # boşluklu
    }

    dates = []
    for format in regex_list.keys():
        matches = re.findall(regex_list[format], text)

        if matches:
            for date in matches:
                dates.append({"value": date, "type": format})

    return dates
